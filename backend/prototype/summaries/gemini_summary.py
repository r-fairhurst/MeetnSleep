import sys
from dotenv import dotenv_values  # pip install python-dotenv
from google import genai

# Configure the api_key and the client for gemini
config = dotenv_values("KEY.env")
api_key = config.get("GEMINI_KEY")
client = genai.Client(api_key=api_key)

# Sample meeting transcript generated via ChatGPT
text = """
Good morning, everyone. Let's get started. First on the agenda, the marketing team has been working on the new campaign, and Sarah, could you give us a quick update?
Sure! We've finalized the designs, and the content is almost ready. We expect to launch by the end of next week.
Great! Next, the development team. John, how's the progress on the new feature?
We're about 80% done. We still need to finalize testing, but everything looks good so far.
Awesome. Let's aim for a final review by Friday. Does that timeline work for everyone?
Yes, that should be fine.
Perfect. Finally, on operations, we’ve been getting some customer feedback about response times. Lisa, can you look into that?
Yes, I'll analyze the data and propose some improvements by the next meeting.
Sounds good. Any other topics before we wrap up?
Nope, that covers everything.
Alright, thanks, everyone! See you next week.
"""

prompt = "Please summarize the following meeting transcript and capture all main ideas succinctly: " + text

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt,
)

print(response.text)