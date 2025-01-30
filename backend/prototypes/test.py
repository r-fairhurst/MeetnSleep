# Speech Recognition
# Dependencies: pip install SpeechRecognition

# Use microphone instead of audio file 

import pyaudio
import wave
import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.AudioFile('test.wav') as source:
    audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        print("Transcript:", text)
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition.")
