# 1. How to install Minute-Meet

### Prerequisites
- Python 3.10 or greater
- Git

### Required Python Packages
- SpeechRecognition
- ffmpeg
- Fastapi
- Unicorn
- Uvicorn
- tqdm
- python-Levenshtein
- python-dotenv
- google-genai
- protobuf
- transformers
- torch
- sentencepiece
- openai
- pyaudio
- pytest
- django
- flake8

### Cloning the Repository and installing the required packages
To install Minute-Meet, you will need to clone the repository and install the required packages. 

```bash
git clone https://github.com/r-fairhurst/MeetnSleep
```

cd into the main directory

```bash
cd MeetnSleep
```

Use the following command to install the required packages

**NOTE:** THIS WILL PROBABLY TAKE A FEW MINUTES
```bash
pip install -r requirements.txt
```

#### NOTE:
If neccesary create a python virtual environment to install the required packages.

```
python -m venv "venv"
```

Then activate the virtual environment

```
source venv/bin/activate
```

You can replace venv with any name you want to give the virtual environment.

Then run the commands above to install all the required packages.

# 2. How to run the software.
To run the program, you will need to run the following command in the terminal.

```bash
python frontend/djangoProject/manage.py runserver
```

This should initiallize a local server that you can access by going to the following link in your browser:

```
http://127.0.0.1:8000/minuteMeet
```

# 3. How to use the software

This software is designed for users who are familiar with our platform

**Web Application (work in progress)**

- Open your preferred web browser.

- Navigate to the localhost URL provided

```
http://127.0.0.1:8000/minuteMeet
```

### Transcribing

Currently there are two options for transcription: recording audio through the app or uploading an audio file on the home page.

#### Recording Audio

To record and transcribe audio using the app, follow these steps:

- Press the green "New Recording" button near the top of the home screen.
- A pop-up should appear. As soon as you close it, the recording will start. 
- After navigating to the recording screen, press the "Start Recording" button to begin a new recording.
- When you are finished recording audio, press on the "Stop Recording" button at the bottom of the page.
- Save the transcript to a safe location.

#### Uploading Audio File

To transcribe audio from a file using the app, follow these steps:

- Navigate to the home page.
- View the form at the center of the screen.
- Select the browse option to select a file to upload.
- Choose file with a valid input type (.mp3, .mpega, .mp2, .wav, .oga).
- With a valid file selected press "Upload & Transcribe."
- After the pop-up closes, the file will download.
- Save it in a safe location.

### Summarizing

Summarization is handled through Google's Gemini API and the summarization page.

#### Adding API Key

- Navigate to the home page.
- Press "Settings."
- Get a FREE Gemini API key from the following link:

```
https://aistudio.google.com/apikey
```

- Enter your API key into the text field.
- Select "Submit Gemini API Key."
- Your API key is now stored and ready to use.

#### Summarizing Meeting Files

- Navigate to the "Summaries" page from the home page.
- Select the browse option to select a file to upload.
- Choose file with a valid input type (.txt, .srt).
- With a valid file selected press "Upload & Summarize."
- After a variable amount of time (based on the size of your file) the summary should appear below the upload form with the summarized text available for viewing and downloading.

# 5. Support & Questions

### Found a bug?
If you ever encounter a bug while using our software and want to help us keep our product bug-free then follow these guidelines!

#### Step 1
If you found a bug, make sure you are using the latest software version we have available, and also double check that it is not already listed within the issue tracker found on github: 

```
https://github.com/r-fairhurst/MeetnSleep/issues
```

- **NOTE:** If you do not have an account on GitHub and do not wish to create one you can email one the devs about the bug following the same format.

#### Step 2
Determine the steps required to reproduce the bug.
- This is important as it allows our dev team to reproduce the issue on their own machines.

#### Step 3
Following our bug report template found in this folder named "bug_report_template", a new issue can be created on our github found here: 

```
https://github.com/r-fairhurst/MeetnSleep/issues
```

- **NOTE:** If you do not have an account on GitHub and do not wish to create one you can email one the devs about the bug following the same format.

#### Step 4
Wait for a patch from the dev team and keep an ear out if we need any more information from you.

- Reach out to the maintenance team via isweesin@oregonstate.edu or mortonwi@oregonstate.edu

# 6. Known bugs

- Check the link below for frequently encountered issues:
```
https://github.com/r-fairhurst/MeetnSleep/issues
```
