# INSTRUCTIONS: python bart_summary.py
# pip install transformers torch
from transformers import BartForConditionalGeneration, BartTokenizer

def bartSummary(text, enablePrint):
    # Initialize the BART model and tokenizer
    model_name = "facebook/bart-large-cnn"  # FREE MODEL
    tokenizer = BartTokenizer.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name)

    # Tokenize the input text
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)

    # Generate summary (adjust max_length and min_length as needed)
    summary_ids = model.generate(inputs, max_length=150, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)

    # Decode the summary and print it
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    if (enablePrint != False):
        print("\n\nBART Meeting Summary:")
        print(summary + "\n\n")

    return

bartSummary("TEXT HERE", True)