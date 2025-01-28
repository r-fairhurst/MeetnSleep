# Speech Recognition
# Dependencies: pip install SpeechRecognition

# Use microphone instead of audio file 

import SpeechRecognition as sr

recognizer = sr.Recognizer()
with sr.AudioFile('test.wav') as source:
    audio_data = recognizer.record(source)
    text = recognizer.recognize_google(audio_data)
    print(text)
