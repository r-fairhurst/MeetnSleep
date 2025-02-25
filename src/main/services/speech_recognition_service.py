# src/main/services/speech_recognition_service.py

import speech_recognition as sr
import time
import os
from datetime import timedelta, datetime

recognizer = sr.Recognizer()
stop_listening = False

EXIT_KEYWORD = "fire extinguisher"

def format_timestamp(seconds):
    """Convert seconds to SRT timestamp format (to use it as subtitles later)"""
    td = timedelta(seconds=seconds)
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{td.microseconds//1000:03d}"

def listen_for_speech():
    global stop_listening
    transcript_segments = []
    
    try:
        with sr.Microphone() as source:
            print("About to start listening...")

            # listen ambient noise duration to 1 second for faster startup
            recognizer.adjust_for_ambient_noise(source, duration=1)

            start_time = time.time()
            segment_start_time = start_time
            segment_number = 1

            while not stop_listening:
                try:

                    audio = recognizer.listen(source, timeout=30, phrase_time_limit=60)
                    text = recognizer.recognize_google(audio)

                    if EXIT_KEYWORD.lower() in text.lower():
                        stop_listening = True
                        break

                    current_time = time.time()
                    segment = {
                        'number': segment_number,
                        'start_time': format_timestamp(segment_start_time - start_time),
                        'end_time': format_timestamp(current_time - start_time),
                        'text': text
                    }
                    
                    transcript_segments.append(segment)
                    print(f"Transcribed: {text}")
                    
                    segment_start_time = current_time
                    segment_number += 1

                except sr.RequestError as e:
                    print(f"Speech recognition service error: {e}")
                    continue
                except sr.WaitTimeoutError:
                    print("No speech detected, continuing to listen...")
                    continue
                except Exception as e:
                    print(f"Unexpected error during transcription: {e}")
                    continue

        if transcript_segments:
            save_transcript(transcript_segments)
            return " ".join(segment['text'] for segment in transcript_segments)
            
    except Exception as e:
        print(f"Error in speech recognition setup: {e}")
    
    return None

def save_transcript(transcript_segments, file_prefix="meeting_transcript"):

    try:
        os.makedirs("storage/transcripts", exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{file_prefix}_{timestamp}.srt"
        filepath = os.path.join("storage/transcripts", filename)
        
        with open(filepath, "w", encoding="utf-8") as f:
            for segment in transcript_segments:
                f.write(f"{segment['number']}\n")
                f.write(f"{segment['start_time']} --> {segment['end_time']}\n")
                f.write(f"{segment['text']}\n\n")
        
        print(f"Transcript saved: {filepath}")
        
    except Exception as e:
        print(f"Error saving transcript: {e}")

def reset_listening():
    """Reset the stop_listening flag"""
    global stop_listening
    stop_listening = False

# TEST FUNC
def transcribe_audio(file_path):
    """Transcribe audio from a given file and return the text."""
    try:
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)
            return recognizer.recognize_google(audio)
    except Exception as e:
        # print(f"Error transcribing {file_path}: {e}")
        return None
