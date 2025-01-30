# Dependencies: 
#   pip install SpeechRecognition
#   pip install pyaudio

import sys
import pyaudio
import wave
import speech_recognition as sr

def transcribe_audio(filename):
    try:
        recognizer = sr.Recognizer()
        with sr.AudioFile(filename) as source:
            audio_data = recognizer.record(source)

            try:
                text = recognizer.recognize_google(audio_data)
                print("Transcript:", text)
            except sr.UnknownValueError:
                print("ERROR: Could not understand the audio.")
            except sr.RequestError:
                print("ERROR: Could not request results from Google Speech Recognition.")
    except FileNotFoundError:
        print("ERROR: File " + filename + " was not found.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ERROR: No audio file provided.")
        print("USAGE: python test.py <audio_file>")
        sys.exit(1)
    filename = sys.argv[1]
    
    transcribe_audio(filename)
