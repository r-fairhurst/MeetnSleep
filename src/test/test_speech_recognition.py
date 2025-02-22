import pytest
import json
import os
import sys
from tqdm import tqdm
import Levenshtein  # pip install python-Levenshtein

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main.services.speech_recognition_service import transcribe_audio

# RUN WITH pytest OR pytest -s

@pytest.fixture(scope="module")
def expected_outputs():
    """Fixture to load expected outputs before running tests."""
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    expected_outputs_path = os.path.join(base_dir, "test", "test_transcription_inputs", "expected_outputs.json")
    with open(expected_outputs_path, "r") as f:
        outputs = json.load(f)
    return outputs

@pytest.fixture(scope="module")
def test_folder():
    """Fixture to get the path to the folder containing test audio files."""
    return os.path.join(os.path.dirname(__file__), "test_transcription_inputs")

def setUp(self):
    """Load expected outputs before running tests."""
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    expected_outputs_path = os.path.join(base_dir, "test", "test_transcription_inputs", "expected_outputs.json")
    with open(expected_outputs_path, "r") as f:
        self.expected_outputs = json.load(f)

    self.test_folder = os.path.join(os.path.dirname(__file__), "test_transcription_inputs")

def calculate_similarity(expected, actual):
    """Calculate transcription accuracy as a percentage using Levenshtein distance."""
    distance = Levenshtein.distance(expected, actual)
    max_len = max(len(expected), len(actual))
    return (1 - distance / max_len) * 100 if max_len > 0 else 100

def test_transcription_accuracy(expected_outputs, test_folder):
    """Test each audio file and print similarity score."""
    total_score = 0
    num_tests = 0

    # This line shows which file is being tested currently
    tqdm.write("\n")

    for filename, expected_text in tqdm(expected_outputs.items(), desc="Testing", ncols=75):
        audio_path = os.path.join(test_folder, filename)
        actual_transcription = transcribe_audio(audio_path)

        assert actual_transcription is not None, f"transcribe_audio returned None for {filename}"

        actual_transcription = actual_transcription.strip()
        similarity_score = calculate_similarity(expected_text.strip(), actual_transcription)
        tqdm.write(f"{filename}: {similarity_score:.2f}% accuracy")

        total_score += similarity_score
        num_tests += 1
        assert similarity_score >= 80, f"Low accuracy: {similarity_score:.2f}% for {filename}"

    if num_tests > 0:
        average_accuracy = total_score / num_tests
        tqdm.write(f"\nAverage Accuracy: {average_accuracy:.2f}%")
