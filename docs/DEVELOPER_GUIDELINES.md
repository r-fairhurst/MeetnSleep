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

There are two different testing suites available, one for transcription and one for summarization. 

## Transcription

The transcription testing suite uses predefined `.wav` audio files with expected outputs.

The `.wav` audio files used for testing can be found at `src/test/test_transcription_inputs/` along 
with the expected outputs.

To run the tests navigate to the `src/test/` directory.
Run the following command:

`python test_live_transcription.py`

The automated tool transcribes the audio file and compares it with the expected output.

## Summarization

# 5. How to add a new test

# 6. How to build a release of the software
