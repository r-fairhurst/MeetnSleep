import sys
import os
import pytest
from tqdm import tqdm

# Add the correct paths for transcription and main modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/test/prototype")))  # transcription module path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))  # main module path

from transcription import transcribe_audio  # Now it can import from backend/prototype
from main.llms.t5_summary import t_five_summary  # Now it can import from src/main

@pytest.fixture(scope="module")
def test_audio_file():
    """Provide a sample audio file for testing."""
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    test_audio_path = os.path.join(base_dir, "test", "test_valid_transcription_inputs", "test1.wav")
    
    assert os.path.exists(test_audio_path), f"Audio file {test_audio_path} does not exist."
    return test_audio_path

def test_transcription_and_summarization(test_audio_file):
    """Test end-to-end transcription and summarization pipeline."""
    
    # Step 1: Transcribe Audio
    transcript = transcribe_audio(test_audio_file)
    assert transcript is not None, "Transcription returned None, expected a valid transcription."
    assert isinstance(transcript, str), f"Expected transcription to be a string, got {type(transcript)}"
    assert len(transcript.strip()) > 0, "Transcription is empty."

    tqdm.write("\nTranscription Successful!")

    # Step 2: Summarize Transcription
    summary, error = t_five_summary(transcript, False)

    # Step 2.1: Check for error
    if error:
        pytest.fail(f"t5_summary raised an exception for {test_audio_file}: {type(error).__name__}: {error}")

    assert summary is not None, "Summary returned None, expected a valid summary."
    assert isinstance(summary, str), f"Expected summary to be a string, got {type(summary)}"
    assert len(summary.strip()) > 0, "Summary is empty."
    
    tqdm.write("\nSummary Successful!")


    tqdm.write(f"Test for {test_audio_file} passed successfully!")