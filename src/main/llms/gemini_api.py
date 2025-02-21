import sys
from dotenv import dotenv_values  # pip install python-dotenv
from google import genai

# Gemini based summary tool
def geminiSummary(text, enablePrint):
    # Configure the api_key and the client for gemini
    # requires KEY.env file in the same directory
    config = dotenv_values("KEY.env")
    api_key = config.get("GEMINI_KEY")
    client = genai.Client(api_key=api_key)

    prompt = "Please summarize the following meeting transcript and capture all main ideas succinctly: " + text

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )

    if (enablePrint != False):
        print("\n\nGemini Meeting Summary:")
        print(response.text + "\n\n")
    
    return

geminiSummary("TEXT HERE", True)