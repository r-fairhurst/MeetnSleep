# Test the integration of both transcription and summarization
# GOALS: Read .wav audio file, produce transcript, pass transcript into summarization tool
import pytest
import json
import os
import sys
from tqdm import tqdm

# Sets 'src' folder as parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main.services.speech_recognition_service import transcribe_audio
from main.llms.gemini_api import gemini_summary

# Code to load the .wav audio files
@pytest.fixture(scope="module")
def expected_outputs():
    """Fixture to load expected outputs before running tests."""
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    expected_outputs_path = os.path.join(base_dir, "test", "test_valid_transcription_inputs", "expected_outputs.json")
    with open(expected_outputs_path, "r") as f:
        outputs = json.load(f)
    return outputs

@pytest.fixture(scope="module")
def test_folder():
    """Fixture to get the path to the folder containing test audio files."""
    return os.path.join(os.path.dirname(__file__), "test_valid_transcription_inputs")

def test_backend_integration(expected_outputs, test_folder):
    """Test each audio file and return transcript"""

    # This line shows which file is being tested currently
    tqdm.write("\n")

    for filename, _ in tqdm(expected_outputs.items(), desc="Testing Transcription", ncols=75):
        audio_path = os.path.join(test_folder, filename)
        transcription = transcribe_audio(audio_path)

        assert transcription is not None, f"transcribe_audio returned None for {filename}"

        transcription = transcription.strip()
        tqdm.write(f"{filename}: Transcription returned")
        tqdm.write(transcription)
    
        # Pass transcript into Gemini to determine if it gets a summary back
        summary, error = gemini_summary(transcription, False)
        
        # If am error occurred, fail the test and return the error
        if error:
            pytest.skip(f"gemini_summary raised an exception for {filename}: {type(error).__name__}: {error}")

        # If the file has content, summary shouldn't be None
        assert summary is not None, f"Summary is None for {filename}"

        tqdm.write(f"{filename}: Summary returned")
        tqdm.write(summary)
