# INSTRUCTIONS: python t5_summary.py
# pip install transformers torch
# pip install sentencepiece
from transformers import T5Tokenizer, T5ForConditionalGeneration

#summary tool takes in a meeting transcript (text), and a boolean(enablePrint)
#enablePrint determines if the summary should be printed (TRUE) or not (FALSE)
def t_five_summary(text, enablePrint):
    '''This uses an older T5 model to construct summaries'''
    #set the max output length to always be 150
    max_output_length=150

    try:
        # Load the model and tokenizer
        tokenizer = T5Tokenizer.from_pretrained('t5-large', legacy=False)
        model = T5ForConditionalGeneration.from_pretrained('t5-large')
        
        # Prepare input text for summarization
        input_text = "summarize main ideas: " + text
        input_ids = tokenizer.encode(input_text, return_tensors='pt', max_length=512, truncation=True)
        
        # Generate summary
        summary_ids = model.generate(input_ids, max_length=max_output_length, num_beams=5, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        
        #if print is enabled, then print to the client the meeting summary
        if (enablePrint):
            print("\n\nT5 Meeting Summary:")
            print(summary + "\n\n")

        #Return the summary and null
        return summary, None
    
    except (OSError, ValueError, RuntimeError, TypeError) as e:
        '''Return no summary and the error as e'''
        return None, e