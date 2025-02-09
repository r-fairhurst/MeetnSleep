# Dependencies: 
#   pip install SpeechRecognition
#   pip install pyaudio

import sys
import pyaudio
import wave
import speech_recognition as sr

'''
TODO:
[DONE] Test scripts using a data set of expected outputs and inputs
[DONE] Determine the success rate of the program
[Done] Update for microphone access
Provide backend cli interface
'''

def transcribe_audio():
    transcript = ""
    text = ""
    running = True
    while running:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            audio_data = recognizer.record(source, duration=5)
            try:
                text = recognizer.recognize_google(audio_data)
                transcript = transcript + " " +text
            except sr.UnknownValueError:
                print("ERROR: Could not understand the audio.")
                return None
            except sr.RequestError:
                print("ERROR: Could not request results from Google Speech Recognition.")
                return None
        print(text)
        if "stop test" in text.lower():
            running = False
    return transcript


if __name__ == "__main__":
    
    text = transcribe_audio()
    print("Full Transcript:",text)