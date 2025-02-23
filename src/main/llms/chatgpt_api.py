# src/main/llms/chatgpt_api.py
import os
import sys
from openai import OpenAI
from main.services.speech_recognition_service import (
    listen_for_speech,
    reset_listening,
    EXIT_KEYWORD
)

# setup the api key
def setup_openai_client():
    api_key = os.getenv("CHATGPT_API")
    if not api_key:
        print("OpenAI API key not found. Please set it as an environment variable.")
        sys.exit(1)
    return OpenAI(api_key=api_key)

# chatgpt summary and speech recognition
def openai_summary(enablePrint):
    # setup the key again for the test case

    api_key = os.getenv("CHATGPT_API")
    if not api_key:
        print("OpenAI API key not found. Please set it as an environment variable.")
        return None, None 
    
    # send the main prompt 
    # TODO: more instructions needed to be implemeneted
    client = setup_openai_client()
    messages = [
        {"role": "system", "content": """
        Summarize the meeting in bullet points with **bolding** for important information.
        * Don't talk like an agent, your only job to summarize the text you get like a normal software
        """}
    ]
    # break and summarize if the keyword is used
    print(f"Listening for the meeting: Use '{EXIT_KEYWORD}' to stop and get a summary.")

    reset_listening()
    text = listen_for_speech()
    if not text:
        print("No transcript generated. Exiting...")
        return None, None  # return a tuple for consistency

    print("\nGenerating meeting summary...")
    messages.append({"role": "user", "content": text})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            stream=False,
            temperature=0.8,
            max_tokens=1000
        )
        if response and response.choices:
            summary = response.choices[0].message.content
            if enablePrint:
                print("\nOpenAI Meeting Summary:\n")
                print(summary)
            return summary, None
        else:
            print("No response received from OpenAI.")
            return None, None

    except Exception as e:
        print(f"OpenAI API Error: {e}")
        return None, e

def main():
    openai_summary(True)

if __name__ == "__main__":
    summary, error = main(True)
    if error:
        print(f"Error: {error}")