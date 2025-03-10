import os
import sys
import json
import time
import pyaudio
from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse, StreamingHttpResponse, FileResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Get the absolute path of 'src/main/services' and add it to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src/main/services")))

from summarization import summarize_transcript, save_summarized_transcript
from speech_recognition_service import listen_for_speech, transcribe_audio, start_recording, stop_recording, get_flag
# from src.main.services.speech_recognition_service import listen_for_speech, transcribe_audio

# This should be a very temporary fix
# Global variable to control streaming
transcription_active = False 

# Create your views here.
def home(request):
    return render(request, 'home.html')

def recordingPage(request):
    return render(request, "recording.html")

def archivePage(request):
    return render(request, "archive.html")

def settingsPage(request):
    return render(request, 'settings.html')

def summaryPage(request):
    summaries = list_summaries(request)
    if not summaries:
        return render(request, "summary.html", {"error": "Error loading summaries."})
    return render(request, "summary.html", {"summaries": summaries})


# used to stop the transcription
@csrf_exempt
def stop_transcription(request):
    '''endpoint to stop recording'''
    if request.method in ["POST", "GET"]:
        print("Stopping Transcription...")
        try:
            stop_recording()
            print("Transcription stopped.")
            return JsonResponse({"success": True})
        except Exception as e:
            print(f"Error stopping recording: {str(e)}")
            return JsonResponse({"success": False, "error": str(e)}, status=500)
    
    return JsonResponse({"error": "Invalid request method."}, status=400)


# used to start the transcription
@csrf_exempt
def start_transcription(request):
    '''endpoint to start live speech recognition'''
    if request.method == "POST":
        start_recording()
        print("Starting Transcription...")
        transcript = listen_for_speech()
        if transcript:
            return JsonResponse({"success": True, "transcript": transcript})
        return JsonResponse({"success": False, "message": "No speech detected or error occurred."})
    
    return JsonResponse({"error": "Invalid request method."}, status=400)


# used to upload
@csrf_exempt
def upload_audio_transcription(request):
    '''endpoint to transcribe uploaded audio files and return them as a .txt'''
    if request.method == "POST" and request.FILES.get("audio_file"):
        audio_file = request.FILES["audio_file"]
        temp_file_path = f"storage/uploads/temp_{audio_file.name}"

        os.makedirs("storage/uploads", exist_ok=True)
        with open(temp_file_path, "wb+") as destination:
            for chunk in audio_file.chunks():
                destination.write(chunk)

        transcript = transcribe_audio(temp_file_path)

        if transcript:
            response = HttpResponse(transcript, content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename="transcript.txt"'
            os.remove(temp_file_path)
            return response

        os.remove(temp_file_path)

        return JsonResponse({"success": False, "message": "Could not transcribe the audio."})

    return JsonResponse({"error": "No audio file provided."}, status=400)


# used to stream the transcription to the frontend
@csrf_exempt
def stream_transcription(request):
    """Stream transcription data while recording."""
    global transcription_active
    transcription_active = True  # Set to active when starting
    
    # Get the selected device index from the query parameter
    device_index = request.GET.get("device_index")
    if device_index:
        try:
            device_index = int(device_index)
            print(f"Starting Transcription Stream with device index: {device_index}...")
        except ValueError:
            print(f"Invalid device index: {device_index}, using default device")
            device_index = None
    else:
        device_index = None
        print("Starting Transcription Stream with default device...")
    
    start_recording()   # Set the flag within the backend

    def event_stream():
        # Pass the device index to listen_for_speech
        for segment in listen_for_speech(device_index=device_index):
            if not transcription_active:
                print("Transcription stopped, exiting stream.")
                break
            yield f"data: {json.dumps(segment)}\n\n"
            time.sleep(1)

    return StreamingHttpResponse(event_stream(), content_type="text/event-stream")


# used to stop transcription 
@csrf_exempt
def stop_transcription_stream(request):
    """Stops the live transcription stream."""
    global transcription_active     # Set flag here in frontend
    stop_recording()                # Set flag within actual backend transcription

    if request.method == "POST":
        transcription_active = False
        print("Stopping Transcription Stream...")
        return JsonResponse({"success": True, "message": "Transcription stopped."})
    
    return JsonResponse({"error": "Invalid request method."}, status=400)


# used to list the summaries of the transcript files
@csrf_exempt
def list_summaries(request):
    summaries = []
    try:
        summaries_dir = os.path.join(os.path.dirname(__file__), "../../../storage/summaries")
        os.makedirs(summaries_dir, exist_ok=True)
        summary_files = [f for f in os.listdir(summaries_dir) if f.endswith('.txt')]
        for file in summary_files:
            file_path = os.path.join(summaries_dir, file)
            stats = os.stat(file_path)
            summaries.append({
                'name': file,
                'path': f"{summaries_dir}/{file}",  # Update path to URL
                'size': stats.st_size,
                'created': datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
            })
    except Exception as e:
        print(f"Error loading summaries: {str(e)}")
        return 
    return summaries


# the download_summary function is used to download the summary files, but doesn't work right now
@csrf_exempt
def download_summary(request, file_name):
    file_path = os.path.join(os.path.dirname(__file__), "../../../storage/summaries", file_name)
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=file_name)
        return response
    else:
        return JsonResponse({"error": "File not found."}, status=404)


# used to upload the transcript file and summarize it
@csrf_exempt
def upload_transcript(request):
    if request.method == "POST" and request.FILES.get("textFile"):
        text_file = request.FILES["textFile"]
        file_path = f"storage/summaries/{text_file.name}"

        os.makedirs("storage/summaries", exist_ok=True)
        with open(file_path, "wb+") as destination:
            for chunk in text_file.chunks():
                destination.write(chunk)

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                transcript_content = file.read()
            
            summary = summarize_transcript(transcript_content, enablePrint=False)
            if not summary:
                return JsonResponse({"success": False, "message": "Could not summarize the transcript."})
            
            summary_file_path = file_path.replace(".srt", "_summary.txt").replace(".txt", "_summary.txt")
            save_summarized_transcript(summary, summary_file_path)

            # After successfully saving the summary, return a response with redirect info
            return JsonResponse({
                "success": True, 
                "summary_path": summary_file_path,
                "redirect": "/minuteMeet/summaryPage/"
            })
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})

    return JsonResponse({"error": "No text file provided."}, status=400)


# used to view the summary of the transcript
@csrf_exempt
def view_summary(request, file_name):
    file_path = os.path.join(os.path.dirname(__file__), "../../../storage/summaries", file_name)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return HttpResponse(content, content_type='text/plain')
    else:
        return JsonResponse({"error": "File not found."}, status=404)
    

# used to let user upload the transcript key
@csrf_exempt
def upload_transcript_key(request):
    if request.method == "POST":
        transcript_key = request.POST.get("textKeyInput")
        if not transcript_key:
            return JsonResponse({"success": False, "message": "No transcript key provided."})
        
        path_to_key = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src/main/llms/KEY.env"))
        try:
            with open(path_to_key, "w") as key_file:
                key_file.write(f"GEMINI_KEY={transcript_key}")
            return JsonResponse({"success": True, "message": "Transcript key successfully saved."})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})
    
    return JsonResponse({"error": "Invalid request method."}, status=400)


# used to get the input devices
@csrf_exempt
def get_input_devices(request):
    """Endpoint to get the list of input devices."""
    if request.method == "GET":
        p = pyaudio.PyAudio()
        device_count = p.get_device_count()
        
        # Use a dict to track unique devices by name
        unique_devices = {}
        for i in range(device_count):
            device_info = p.get_device_info_by_index(i)
            device_name = device_info.get("name")
            # Only add if it's not already in our list
            if device_name not in unique_devices:
                unique_devices[device_name] = {"index": i, "name": device_name}
        
        # Convert to list
        devices = list(unique_devices.values())
        # Add desktop audio as an option
        devices.append({"index": -1, "name": "Desktop Audio"})
        
        p.terminate()
        return JsonResponse({"success": True, "devices": devices})
    return JsonResponse({"error": "Invalid request method."}, status=400)
