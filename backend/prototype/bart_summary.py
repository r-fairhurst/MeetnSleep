from transformers import BartForConditionalGeneration, BartTokenizer

# Initialize the BART model and tokenizer
model_name = "facebook/bart-large-cnn"  # FREE MODEL
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

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

# Tokenize the input text
inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)

# Generate summary (adjust max_length and min_length as needed)
summary_ids = model.generate(inputs, max_length=150, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)

# Decode the summary and print it
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
print("Summary:", summary)
