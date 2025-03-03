import os
import sys
from datetime import datetime

# Add the parent directory to the path to access the llms module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "llms")))

# Import the gemini_summary function from gemini_api module
from gemini_api import gemini_summary
import argparse

def summarize_transcript(transcript, enablePrint):
    '''Summarize the transcript using the Gemini API'''
    # Get the current time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"Summarizing transcript at {current_time}...")
    summarized_transcript, error = gemini_summary(transcript, enablePrint)
    if error:
        print(f"Error summarizing transcript: {error}")
        return None
    print("Transcript summarized.")

    return summarized_transcript


def get_transcript_to_summarize(transcript_file_path):
    """
    Reads the transcript from a file and passes it to the
      summarize_transcript function.
    
    Args:
        transcript_file_path: Path to the transcript file
    
    Returns:
        The summarized transcript
    """
    try:
        with open(transcript_file_path, 'r', encoding='utf-8') as file:
            transcript_content = file.read()
            return transcript_content
    except FileNotFoundError:
        print(f"Error: File not found at {transcript_file_path}")
    except Exception as e:
        print(f"Error reading transcript file: {e}")
    return None


def save_summarized_transcript(summarized_transcript, output_file_path):
    """
    Save the summarized transcript to a file.
    
    Args:
        summarized_transcript: The summarized transcript
        output_file_path: Path to save the summarized transcript
    """
    try:
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(summarized_transcript)
    except Exception as e:
        print(f"Error saving summarized transcript: {e}")

def parse_arguments():
    """
    Parse command line arguments for transcript file path.
    
    Returns:
        The parsed arguments with the transcript file path.
    """
    parser = argparse.ArgumentParser(description='Summarize a transcript file.')
    parser.add_argument('--file', '-f', type=str, required=True, 
                        help='Path to the transcript file to summarize')
    return parser.parse_args()


def main():
    # Parse arguments to get the transcript file path
    args = parse_arguments()
    transcript_file_path = args.file
    
    # Get the transcript content
    transcript_content = get_transcript_to_summarize(transcript_file_path)
    
    if transcript_content:
        # Summarize the transcript
        summary = summarize_transcript(transcript_content, True)
        if summary:
            print("\nSummarized Transcript:")
            # Save the summarized transcript
            save_summarized_transcript(summary, transcript_file_path.replace(".srt", "_summary.txt"))


if __name__ == "__main__":
    main()