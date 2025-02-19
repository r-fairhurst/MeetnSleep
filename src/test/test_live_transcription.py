import unittest
import json
import os
import sys
from tqdm import tqdm
import Levenshtein  # pip install python-Levenshtein

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main.services.speech_recognition_service import transcribe_audio

class TestTranscription(unittest.TestCase):
    def setUp(self):
        """Load expected outputs before running tests."""
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        expected_outputs_path = os.path.join(base_dir, "test", "test_transcription_inputs", "expected_outputs.json")
        with open(expected_outputs_path, "r") as f:
            self.expected_outputs = json.load(f)

        self.test_folder = os.path.join(os.path.dirname(__file__), "test_transcription_inputs")
        
        # Debugging statements
        # print("EXPECTED OUTPUTS PATH: " + expected_outputs_path)
        # print("TEST FOLDER PATH: " + self.test_folder)

    def calculate_similarity(self, expected, actual):
        """Calculate transcription accuracy as a percentage using Levenshtein distance."""
        distance = Levenshtein.distance(expected, actual)
        max_len = max(len(expected), len(actual))
        return (1 - distance / max_len) * 100 if max_len > 0 else 100

    def test_transcription_accuracy(self):
        """Test each audio file and print similarity score."""
        total_score = 0
        num_tests = 0

        for filename, expected_text in tqdm(self.expected_outputs.items(), desc="Testing", ncols=75):
            audio_path = os.path.join(self.test_folder, filename)
            actual_transcription = transcribe_audio(audio_path)

            if actual_transcription is None:
                self.fail(f"transcribe_audio returned None for {filename}")

            actual_transcription = actual_transcription.strip()
            similarity_score = self.calculate_similarity(expected_text.strip(), actual_transcription)
            tqdm.write(f"{filename}: {similarity_score:.2f}% accuracy")

            total_score += similarity_score
            num_tests += 1
            self.assertGreaterEqual(similarity_score, 80, f"Low accuracy: {similarity_score:.2f}% for {filename}")

        if num_tests > 0:
            average_accuracy = total_score / num_tests
            tqdm.write(f"\nAverage Accuracy: {average_accuracy:.2f}%")

if __name__ == "__main__":
    unittest.main()
