Developer Guidelines


# 1. How to Obtain the Source Code

## Clone the Repository
    
        git clone https://github.com/r-fairhurst/MeetnSleep.git
        cd meetnsleep
    
## Contribute
To Contribute:
1. Fork the Repository
2. Clone your forked repo:
` git clone https://github.com/r-fairhurst/MeetnSleep.git`
3. Add an upstream remote:
`git remote add upstream https://github.com/r-fairhurst/MeetnSleep.git`
4. Fetch for the latest changes:
`git pull upstream main`

# 2. Directory Structure.

Our main project structure is the following (MVC-style structure):

    meetnsleep
    ├── README.md              # Project overview
    ├── frontend/              # Frontend code (if applicable)
    │   ├── app.js            # main frontend logic
    │   ├── components/       # reusable components
    │   ├── public/           # Static files
    │   ├── src/              # Source code
    ├── scripts/               # Utility scripts
    ├── src/                   # Main source code for the app
    │   ├── api/              # API routes (to use the Django app)
    │   ├── models/           # Data models
    │   ├── services/         # the app logic
    │   ├── utils/            # Helper functions
    │   ├── tests/            # Unit & integration tests
    ├── storage/               # Storage for files (e.g. transcripts, summaries.)
    └── requirements.txt 

# 3. How to build the software

### Install dependencies
`pip install -r requirements.txt`
### Running the backend
`python src/mainapp.py`

# 4. How to test the software

There are two different testing suites available, one for transcription and one for summarization. These both utilize 
PyTest and can be run using `pytest` or `pytest -s`.

## Transcription

The transcription testing suite uses predefined `.wav` audio files with expected outputs.

The `.wav` audio files used for testing can be found at `src/test/test_transcription_inputs/` along 
with the expected outputs `.json` file.

To run the tests, navigate to the `src/test/` directory and run the following command:

`pytest` or `pytest -s`

PyTest will the the automated tests and determine if they all pass.

If `pytest -s` was executed, the automated tool transcribes the audio file, compares it with the expected output, and 
returns the accuracy as a percentage.

## Summarization

The transcription testing suite uses a predefined `.json` transcription file with expected outputs.

The `.json` transcription files used for testing can be found at `src/test/test_transcription_inputs/expected_outputs.json` along 
with the audio inputs of each in their respective `.wav` file.

To run the tests, navigate to the `src/test/` directory and run the following command:

`python -m pytest test_testname.py`

PyTest will the the automated tests and determine if they all pass.

If `python -m pytest` was executed, the automated tool summarizes the transcription, compares it with the expected output, and 
returns the accuracy as a percentage.

# 5. How to add a new test

Adding a new test requires that the user have a predefined `.wav` audio file and an accurate transcription available
for the audio. It is required that the audio file is in english.

1. Navigate to the `src/test/test_transcription_inputs/` directory. 

2. Add the `.wav` file to this directory.

3. Open the `expected_outputs.json` file and add the file name and accurate transcription in the form:
   `"filename.wav": "transcription text"`
   
5. Test that the file is included in the test suite by executing the test suite as explained in Developer Guidelines
5.

# 6. Current Test Descriptions

### Frontend
- Example Test name
    - **Author:** your name
    - **Goal/Description of test:** words words blah blah blah 
    - **How to execute the test:**, aka pytest, or navigate to it and run it
    
### Backend
- **test_unit_t5_summary.py**
    - **Author:** Aidan Daly
    - **Goal/Description of test:** The goal of this is to test the summarization function that is implemented from the t5 summary api. This test makes sure that valid transcripts will have a summary. It also tests if short transcription files can be converted into summaries. 
    - **How to execute the test:** navigate to MeetnSleep/src/test then run this command: python -m pytest .\test_unit_t5_summary.py
- **test_t5_summarization.py**
    - **Author:** Aidan Daly
    - **Goal/Description of test:** The foal of this is to test the summarization function from the t5 api over many different transcriptions to make sure that all of them are able to be transformed into a summary with the api. Returns any errors if the test fails. 
    - **How to execute the test:** navigate to MeetnSleep/src/test then run this command: python -m pytest .\test_t5_summarization.py
- **test_system_transcription_summary.py**
    - **Author:** Aidan Daly
    - **Goal/Description of test:** This test integrates both the summarization function from our api, and our transcription function, to test the full workflow of our program. This test uses multiple audio recording files (.wav) to transcribe them then summarize them, reporting any issues to the console in teh process. 
    - **How to execute the test:** navigate to MeetnSleep/src/test then run this command: python -m pytest .\test_system_transcription_summary.py
- test_transcript_src_integration
    - **Author:** Aiden Reedy
    - **Goal/Description of test:** This tests to make sure the program saves the files in the correct file type (.srt) and format. This is important because many other parts rely on the file being in that format.
    - **How to execute the test:** navigate to MeetnSleep/src/test then run this command: python -m pytest .\test_transcript_src_integration.py
- test_srt_validation
    - **Author:** Aiden Reedy
    - **Goal/Description of test:** This tests to make sure that the file saving script doesn't save a file if it has the wrong format or other issues like being empty. This is important because many other parts rely on the file being in that format.
    - **How to execute the test:** navigate to MeetnSleep/src/test then run this command: python -m pytest .\test_srt_validation.py
- test_unit_file_saving
    - **Author:** Aiden Reedy
    - **Goal/Description of test:** This tests to make sure the program saves the file to the right location. This is important because other parts of the program like summarization need to access the file.
    - **How to execute the test:** navigate to MeetnSleep/src/test then run this command: python -m pytest .\test_unit_file_saving.py
- test_system_transcription_summary
    - **Author:** William Morton
    - **Goal/Description of test:** This tests the transcription and summarization backend integration. It first gets a valid audio file, transcribes it, and then passes it to summarization. This tests T_5 in particular but it can be swapped out for either the OpenAI or Gemini models.
    - **How to execute the test:** navigate to MeetnSleep/src/test then run this command: python -m pytest .\test_system_transcription_summary.py
- test_gemini_summarization
    - **Author:** William Morton
    - **Goal/Description of test:** This tests the Gemini summary service by passing valid inputs into the API and checking if the returned values are valid. This also checks for thrown exceptions including a missing API key.
    - **How to execute the test:** navigate to MeetnSleep/src/test then run this command: python -m pytest .\test_gemini_summarization.py
- test_transcription
    - **Author:** William Morton
    - **Goal/Description of test:** The purpose of this test is to test the accuracy of the transcription service and also to ensure that the transcription service is working as intended. It does this by testing the transcription outputs against the correct transcription outputs for predefined files.
    - **How to execute the test:** navigate to MeetnSleep/src/test then run this command: python -m pytest .\test_transcription.py

