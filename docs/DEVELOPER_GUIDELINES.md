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

Not yet implemented.

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
    

