# Speech Recognition
# pip install SpeechRecognition
import SpeechRecognition as sr

recognizer = sr.Recognizer()
with sr.AudioFile('test.wav') as source:
    audio_data = recognizer.record(source)
    text = recognizer.recognize_google(audio_data)
    print(text)

    