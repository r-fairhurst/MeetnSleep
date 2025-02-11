# INSTRUCTIONS: python t5_summary.py
# pip install transformers torch
# pip install sentencepiece
from transformers import T5Tokenizer, T5ForConditionalGeneration

def tFiveSummary(text, enablePrint):
    max_length=150

    # Load the model and tokenizer
    tokenizer = T5Tokenizer.from_pretrained('t5-large')
    model = T5ForConditionalGeneration.from_pretrained('t5-large')
    
    # Prepare input text for summarization
    input_text = "summarize main ideas: " + text
    input_ids = tokenizer.encode(input_text, return_tensors='pt', max_length=512, truncation=True)
    
    # Generate summary
    summary_ids = model.generate(input_ids, max_length=max_length, num_beams=5, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    
    if (enablePrint != False):
        print("\n\nT5 Meeting Summary:")
        print(summary + "\n\n")

    return

tFiveSummary("TEXT HERE", True)