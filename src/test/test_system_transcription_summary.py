import os
import sys
import json
import pytest
from tqdm import tqdm

# Add both the root 'MeetnSleep' directory 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))  # Root directory
#Add src directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "src")))  # src directory

#import the t5 summary module
from main.llms.t5_summary import t_five_summary
#import our audio transcription module
from backend.prototype.transcription import transcribe_audio  # Adjust if needed

#Start the test in the scope of the module
@pytest.fixture(scope="module")
def test_audio_files():
    """Load a list of test audio files for system testing."""
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    test_audio_path = os.path.join(base_dir, "test", "test_valid_transcription_inputs")

    # Collect all WAV files for testing
    return [os.path.join(test_audio_path, file) for file in os.listdir(test_audio_path) if file.endswith(".wav")]

def test_system_transcription_summary(test_audio_files):
    """System test for the full transcription and summarization pipeline."""

    output_results = {}
    tqdm.write("\nStarting system test...\n")

    for file_path in tqdm(test_audio_files, desc="System Test", ncols=75):
        assert os.path.exists(file_path), f"Test audio file {file_path} does not exist."

        # Step 1: Transcribe Audio
        transcript = transcribe_audio(file_path)
        assert transcript, f"Transcription failed for {file_path}"

        # Step 2: Summarize the Transcription
        summary = t_five_summary(transcript, False)
        assert summary, f"Summarization failed for {file_path}"

        tqdm.write(f"\nTest passed for: {file_path}")
        
        # Save the results
        output_results[file_path] = {"transcription": transcript, "summary": summary}

    # Save results to a JSON file for further validation
    output_path = os.path.join(os.path.dirname(__file__), "system_test_results.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_results, f, indent=4)

    tqdm.write("\nSystem Test Completed. Results saved to system_test_results.json\n")
