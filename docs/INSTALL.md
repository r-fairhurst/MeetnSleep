# 1. How to install the software

### Prerequisites
- Python >= 3.10
- Git

### Cloning the Repository and installing the required packages
To install the project, you will need to clone the repository and install the required packages. 

```bash
git clone https://github.com/r-fairhurst/MeetnSleep
```

Then cd into the main directory

```bash
cd MeetnSleep
```

Then use the following command to install the required packages

**NOTE:** THIS WILL PROBABLY TAKE A FEW MINS
```bash
pip install -r requirements.txt
```

#### NOTE:
If necessary, create a Python virtual environment to install the required packages.

```
python -m venv "venv"
```

Then activate the virtual environment

```
source venv/bin/activate
```

You can replace venv with any name you want to give the virtual environment.

Then, run the commands above to install all the required packages.

# 2. How to run the software.
To run the program, you will need to run the following command in the terminal.

```bash
python frontend/djangoProject/manage.py runserver
```

This should initialize a local server that you can access by going to the following link in your browser.

# 3. How to use the software

This software is designed for users who are familiar with our platform

**Web Application**
## How To Use The Program

### Accessing the locally hosted site:
- Open your preferred web browser.
- Navigate to the localhost URL provided
```
http://127.0.0.1:8000/minuteMeet
```
**NOTE** while on the site if you are the main page "http://127.0.0.1:8000/ and get a 404 error, make sure you go to the /minuteMeet page. 

### Start A Meeting To Record
- To start a meeting, click the "Start Meeting" button; this is the green circle with a + in the middle. This will have you go to the recording page
- On the recording page, click the "Start Recording" button to start the recording process.
- Once you are done recording, click the "Stop Recording" button to stop the recording process. This is the red square button.
- The transcript will be saved; you can submit it for summary.
   - this file is found in the project's leading directory, in the "storage/transcripts" folder. It will be a .srt file

### Setting up a Gemini API key for summarization 
    1. After installing and running MinuteMeet, click on the settings page on the bottom home page "http://127.0.0.1:8000/minuteMeet/settingsPage/"
    2. Copy and paste your Gemini API key into the text box
    3. Click on "Submit Gemini API Key"
    4. You are all set. It will auto-redirect you back to the home page

### Submit A Transcript For Summarization
**NOTE** You will need a Gemini API key to submit a transcript for summarization. You can get one by going to the following link and signing up for an account.
```
https://ai.google.dev/gemini-api/docs/api-key
```
- To submit a transcript for summarization, click on the "Summaries" button from the main page. This will take you to the summarization page.
- On the summarization page, you can submit a transcript by clicking the "Browse" button and selecting the .txt or .srt file of your transcript 
- Once Selected, click on the "Upload & Summarize" button. This now starts the API call to Gemini, and once the page refreshes, you will see it appear in the table named "Your Summaries"
- then you can either view or download it

### Submitting An Audio File For Transcription
- To submit an audio file for summarization, click the browse button next to "No file selected" and select the audio file you want to submit.
- then click the "Upload & Transcribe" button to submit the audio file for summarization.


# 4. Support & Questions

### Found a bug?
If you ever encounter a bug while using our software and want to help us keep our product bug-free, follow these guidelines!

#### Step 1
If you found a bug, make sure you are using the latest software version we have available, and also double check that it is not already listed within the issue tracker found on GitHub: https://github.com/r-fairhurst/MeetnSleep/issues 
- **NOTE:** If you do not have an account on GitHub and do not wish to create one, you can email one of the devs about the bug following the same format.

#### Step 2
Figure out the steps to reproduce the bug
- this is most useful if the steps are specific and anyone can follow them to reproduce the bug

#### Step 3
Following our bug report template found in this folder named "bug_report_template," a new issue can be created on our GitHub found here: https://github.com/r-fairhurst/MeetnSleep/issues 
- **NOTE:** If you do not have an account on GitHub and do not wish to create one, you can email one of the devs about the bug following the same format. 

#### Step 4
Simply wait for us to fix it, and keep an ear out if we need any more information from you
- Reach out to the maintainers via isweesin@oregonstate.edu, mortonwi@oregonstate.edu, or fairhurr@oregonstate.edu

# 5. Known bugs
- Take a look at our GitHub issues to see if the bug you are experiencing is already listed there
- https://github.com/r-fairhurst/MeetnSleep/issues 
