import sys
import pyaudio
import speech_recognition as sr
import threading
from queue import Queue
from queue import Empty

'''
TODO:
[DONE] Test scripts using a data set of expected outputs and inputs
[DONE] Determine the success rate of the program
[DONE] Update for microphone access
Provide backend CLI interface
'''

RUNNING = True
REC_TO_API = Queue(maxsize=1000)
API_TO_OUT = Queue(maxsize=1000)


def output(f_name):
    global RUNNING, API_TO_OUT
    with open(f_name, "a") as f:
        while RUNNING or not API_TO_OUT.empty():
            try:
                text = API_TO_OUT.get(block=False)  
                f.write(text + "\n")
                if "stop test" in text.lower():
                    RUNNING = False
            except Exception:
                pass


def api_call():
    global RUNNING, REC_TO_API, API_TO_OUT
    recognizer = sr.Recognizer()
    
    while RUNNING or not REC_TO_API.empty():
        try:
            sending = REC_TO_API.get(block=False)  
            text = recognizer.recognize_google(sending)
            API_TO_OUT.put(text)
        except Empty:
            continue  
        except sr.UnknownValueError:
            print("ERROR: Could not understand the audio.")
        except sr.RequestError:
            print("ERROR: Could not request results from Google Speech Recognition.")


def record():
    global RUNNING, REC_TO_API
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        while RUNNING:
            try:
                audio_data = recognizer.record(source, duration=5)
                REC_TO_API.put(audio_data)
            except Exception as e:
                print(f"ERROR: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Proper use: python3 transcription_threading.py <output file name>")
        sys.exit()

    output_filename = sys.argv[1]

    mic_thread = threading.Thread(target=record)
    api_thread = threading.Thread(target=api_call)
    output_thread = threading.Thread(target=output, args=(output_filename,))

    mic_thread.start()
    api_thread.start()
    output_thread.start()

    mic_thread.join()
    api_thread.join()
    output_thread.join()
