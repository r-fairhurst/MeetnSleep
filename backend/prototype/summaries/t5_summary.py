# INSTRUCTIONS: python t5_summary.py
# pip install transformers torch
# pip install sentencepiece
from transformers import T5Tokenizer, T5ForConditionalGeneration

def summarize_meeting(model_name='t5-large', max_length=150):
    # Load the model and tokenizer
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    
    transcript = """
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
    
    # Prepare input text for summarization
    input_text = "summarize: " + transcript
    input_ids = tokenizer.encode(input_text, return_tensors='pt', max_length=512, truncation=True)
    
    # Generate summary
    summary_ids = model.generate(input_ids, max_length=max_length, num_beams=5, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    
    return summary

if __name__ == "__main__":
    summary = summarize_meeting()
    print("Meeting Summary:")
    print(summary)
