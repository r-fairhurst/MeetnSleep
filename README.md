# Minute-Meet
Our product is a meeting summary tool that the user can boot up to listen to a specific program's audio output. The program will listen to the user's microphone and/or meeting software and transcribe the meeting. When the meeting is over, the transcript will be saved, allowing the user to submit it for summarization.

## How to Install Minute-Meet

### Requirements
Requirements are simple. You'll need base Python and Git.

- Python (Version >= 3.10)
- Git

### Build Instructions

To run our software, you'll need the repository on your local device.

First: clone the repository in your terminal (and directory) of choice with:

```bash
git clone https://github.com/r-fairhurst/MeetnSleep
```

then cd into the main directory

```bash
cd MeetnSleep
```

Then, install the required packages with:

**NOTE:** THIS WILL PROBABLY TAKE A FEW MINS
```bash
pip install -r requirements.txt
```

#### NOTE:
If necessary, create a Python virtual environment to install the required packages.

```bash
python -m venv "venv"
```

Then activate the virtual environment:

```bash
source venv/bin/activate
```

You can replace venv with any name you want to give the virtual environment.

## Run Minute-Meet

To run the program, enter the following command in the terminal:

```bash
python frontend/djangoProject/manage.py runserver
```

this should initialize a local server that you can access by going to the following link in your browser.

```
http://127.0.0.1:8000/minuteMeet
```

### Common Installation Issues

If you are having issues with the installation, make sure you have the correct version of python installed. If you are having issues with the installation of the required packages, try running the following command.

```bash
pip install --upgrade pip
```

This will upgrade pip to the latest version, which may fix the issue.

If you encounter an issue installing the required packages, you might be missing a global dependency that the packages need to install. If you are on a Linux system, you can run the following command to install the required dependencies.

```bash
sudo apt-get install python3-dev
```

or if its a specific to building the wheel for pyaudio, your system might be missing the portaudio library. You can install it by running the following command.

```bash
sudo apt-get install portaudio19-dev
```

## More Information
More information the software can be found in the project docs folder. 
This includes: 
 - Steps on using the software
 - The project proposal
 - Bug reporting documentation
 - Developer guidelines.
 - And more...

## Contributors
 - Frontend
    - Ian McKee
        - Site design, documentation, manual testing with Gemini API calls from the software.
    - Arianna Valencia
        - Django setup, CSS styling, and recording button
 - Backend
    - William Morton
        - Gemini API summarization tool, and setting rules for the prompt, general bug fixing, pioneering tests 
    - Aiden Reedy 
        - Speech to text transcription and audio preprocessing optimization 
 - Fullstack
    - Nadir Isweesi
        - Django setup, created API calls to different LLMS
    - Ryan Fairhurst
        - Viewing all local summaries, downloading summaries, and viewing summaries on the site, CI implementation
    - Aidan Daly
        - Summarization integration, both implementing and linking with the backend
