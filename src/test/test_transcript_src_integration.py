import pytest
import os
from unittest.mock import patch
import glob

from services.speech_recognition_service import save_transcript

@pytest.fixture
def mock_transcript_segments():
    return [
        {'number': 1, 'start_time': '00:00:00,000', 'end_time': '00:00:05,000', 'text': 'Hello, test.'},
        {'number': 2, 'start_time': '00:00:05,000', 'end_time': '00:00:10,000', 'text': 'Simulating speech.'}
    ]

def test_save_transcript(mock_transcript_segments, tmp_path):
    # Mocking listen_for_speech behavior
    with patch('services.speech_recognition_service.listen_for_speech') as mock_listen:
        mock_listen.return_value = mock_transcript_segments
        
        # Save transcript to temp path
        save_transcript(mock_transcript_segments, file_prefix="test_transcript")

        # Use glob to find files with the expected prefix
        file_pattern = str(tmp_path / "test_transcript*.srt")
        matching_files = glob.glob(file_pattern)

        # Ensure the file was created
        assert matching_files, "Transcript file was not saved."
        
        file_path = matching_files[0]

        # Verify file content
        with open(file_path, "r", encoding="utf-8") as file:
            file_content = file.read().strip()

        expected_content = "\n".join([
            "1\n00:00:00,000 --> 00:00:05,000\nHello, test.\n",
            "2\n00:00:05,000 --> 00:00:10,000\nSimulating speech.\n"
        ]).strip()

        assert file_content == expected_content
