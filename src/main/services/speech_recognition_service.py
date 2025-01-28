import speech_recognition as sr
import time
import os
from datetime import timedelta, datetime

recognizer = sr.Recognizer()


def format_timestamp(seconds):
    """Convert seconds to SRT timestamp format to let users sink it with videoa aferward, like movies"""
    td = timedelta(seconds=seconds)
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{td.microseconds//1000:03d}"


def listen_for_speech():

    try:   # keep running for 5 hours
        with sr.Microphone() as source:
            print("Listening...")
            # listen to the background noise for X duration, and then try to to minimize the noise
            recognizer.adjust_for_ambient_noise(source, duration=5)

            duration = 5*60*60
            start_time = time.time()

            transcript_segments = []
            segment_start_time = start_time
            segment_number = 1

            # loop until it is 5 hours

            while time.time() - start_time < duration:
                try:
                    audio = recognizer.listen(source, timeout=120, phrase_time_limit=60)
                    text = recognizer.recognize_google(audio)

                    current_time = time.time()

                    transcript_segments.append({
                        'number': segment_number,
                        'start_time': format_timestamp(segment_start_time - start_time),
                        'end_time': format_timestamp(current_time - start_time),
                        'text': text
                    })
                    
                    print(f"Transcribed: {text}")
                    segment_start_time = current_time
                    segment_number += 1

                except sr.RequestError:
                    print("Sorry, there was an error with the speech recognition service.")
                    continue
                except sr.WaitTimeoutError:
                    print(f"No speech was detected for more than 2 minutes")
                    continue
                finally:
                    if transcript_segments:
                        save_transcript(transcript_segments, f"meeting_transcript_{datetime.now().strftime('%Y%m%d_%H%M%S')}.srt")

        save_transcript(transcript_segments, f"meeting_transcript_{datetime.now().strftime('%Y%m%d_%H%M%S')}.srt")
    except Exception as e:
            print(f"An unexpected error occurred: {e}")

def save_transcript(transcript_segments, filename):
    os.makedirs("storage/transcripts", exist_ok=True)
    filepath = os.path.join("storage/transcripts", filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        for segment in transcript_segments:
            f.write(f"{segment['number']}\n")
            f.write(f"{segment['start_time']} --> {segment['end_time']}\n")
            f.write(f"{segment['text']}\n\n")
    
    print(f"Transcript saved: {filepath}")