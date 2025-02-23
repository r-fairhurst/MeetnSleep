# src/main/llms/chatgpt_api.pyimport os
import sys
from openai import OpenAI
from services.speech_recognition_service import (
    listen_for_speech,
    reset_listening,
    EXIT_KEYWORD
)

def setup_openai_client():

    api_key = os.getenv("CHATGPT_API")
    if not api_key:
        print("OpenAI API key not found. Please set it as an environment variable.")
        sys.exit(1)
    return OpenAI(api_key=api_key)

def main():
    client = setup_openai_client()
    
    # System message for summary generation
    messages = [
        {"role": "system", "content": f"""
        Summarize the meeting in bullet points with **bolding** for important information.
        * Don't talk like an agent, your only job to summarize the text you get like a normal software
        """}
    ]

    print(f"Listening for the meeting: Use '{EXIT_KEYWORD}' to stop and get a summary.")
    
    # Reset listening flag in case of previous runs
    reset_listening()
    
    # Start listening
    text = listen_for_speech()
    
    if not text:
        print("No transcript generated. Exiting...")
        return

    print("\nGenerating meeting summary...")
    
    # Add transcript to messages for summary generation
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
            print("\nMeeting Summary:")
            print(summary)
            
            messages.append({"role": "assistant", "content": summary})
        else:
            print("No response received from OpenAI.")
            
    except Exception as e:
        print(f"OpenAI API Error: {e}")

if __name__ == "__main__":
    main()