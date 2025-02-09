import sys
from dotenv import dotenv_values  # pip install python-dotenv
from openai import OpenAI         # pip install openai

config = dotenv_values("KEY.env")

api_key = config.get("OPENAI_KEY")

client = OpenAI(
  api_key=api_key
)

def sendTranscript(transcript):
  queryString = "Please summarize the following meeting transcript and capture all main ideas succinctly: " + transcript

  completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
      {"role": "user", 
      "content": queryString}
    ]
  )

  return queryString # completion.choices[0].message

if __name__ == "__main__":
  if len(sys.argv) < 2:
      print("Error: No video file provided. Usage: python open_ai_summary.py <transcript>")
      sys.exit(1)

  transcript = sys.argv[1]
  print(sendTranscript(transcript))
