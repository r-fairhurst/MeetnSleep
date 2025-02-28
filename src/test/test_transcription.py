import sys
import os
import pytest

# Test the behavior of transcribe_audio in transcribe.py

# Add the backend/prototype directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../backend/prototype')))

try:
    from transcription import transcribe_audio
except ImportError:
    raise ImportError("Could not import 'transcription' module. Ensure that 'backend/prototype/transcription.py' exists.")

def test_transcribe_audio():
    # Construct a platform-independent file path
    test_audio_file = os.path.join(os.path.dirname(__file__), "test_valid_transcription_inputs", "test1.wav")

    # Debug: Print file path
    print(f"Checking file at: {test_audio_file}")
    
    # Ensure file exists before running the test
    assert os.path.exists(test_audio_file), f"File not found: {test_audio_file}"

    # Call transcribe_audio and assert the result is a string
    result = transcribe_audio(test_audio_file)
    assert isinstance(result, str), "The transcription result should be a string"
    assert len(result) > 0, "The transcription result should not be empty"

def test_transcribe_audio_file_not_found():
    # Test for a file that does not exist
    result = transcribe_audio('non_existent_audio.wav')
    assert result is None, "Should return None for non-existent audio file"
