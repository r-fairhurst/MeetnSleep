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

def transcribe_audio(device_index):
    transcript = ""
    text = ""
    running = True
    while running:
        recognizer = sr.Recognizer()
        with sr.Microphone(device_index=device_index) as source:
            audio_data = recognizer.record(source, duration=5)
            try:
                text = recognizer.recognize_google(audio_data)
                transcript = transcript + " " + text
            except sr.UnknownValueError:
                print("ERROR: Could not understand the audio.")
                return transcript
            except sr.RequestError:
                print("ERROR: Could not request results from Google Speech Recognition.")
                return transcript
        print(text)
        if "stop test" in text.lower():
            running = False
    return transcript


if __name__ == "__main__":
    
    # This will print the possible device options
    # List available microphones
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"Device {index}: {name}")

    # Set this to the preferred audio input index
    device_index = 2

    text = transcribe_audio(device_index)
    print("Full Transcript:",text)