# Minute-Meet
Our product is a meeting summary tool that the user can boot up to listen to a specific program's audio output. The program will listen to the users microphone and or meeting software, transcribe the meeting. When the meeting is over the transcript will then save, allowing the user to submit it for summarization.

## Current Use Cases

### Transcription
Users should be able to transcribe their meetings using the transcription/recording tool.

### Summarization
Users should be able to get summaries of their .srt transcripts using the summary tool.

## Installation Steps

### Prerequisites
- Python >= 3.10
- Git

### Cloning The Repository And Installing The Required Packages
To install the project, you will need to clone the repository and install the required packages. 

```bash
git clone https://github.com/r-fairhurst/MeetnSleep
```

then cd into the main directory

```bash
cd MeetnSleep
```

then use the following command to install the required packages

**NOTE:** THIS WILL PROBABLY TAKE A FEW MINS
```bash
pip install -r requirements.txt
```

#### NOTE:
If neccesary create a python virtual environment to install the required packages.

```bash
python -m venv "venv"
```

then activate the virtual environment

```bash
source venv/bin/activate
```

you can replace venv with any name you want to give the virtual environment.

then run the commands above to install all the required packages.

## Running The Program

To run the program, you will need to run the following command in the terminal.

```bash
python frontend/djangoProject/manage.py runserver
```

this should initiallize a local server that you can access by going to the following link in your browser.

```
http://127.0.0.1:8000/minuteMeet
```

### Common Installation Issues

if you are having issues with the installation, make sure you have the correct version of python installed. If you are having issues with the installation of the required packages, try running the following command.

```bash
pip install --upgrade pip
```

this will upgrade pip to the latest version, which may fix the issue.

if its an issue while installing the required packages, you might be missing a global dependecy that the packages need to install. If you are on a linux system, you can run the following command to install the required dependecies.

```bash
sudo apt-get install python3-dev
```

or if its a specific to building the wheel for pyaudio, your system might be missing the portaudio library. You can install it by running the following command.

```bash
sudo apt-get install portaudio19-dev
```

## More Information
More information can be found in the docs folder of the project. This includes the project proposal, bug reporting documentation, as well as developer guidelines.

## Contributors
 - Frontend
    - Ian McKee
        - site design, manual testing API calls through our software to Gemini API 
    - Arianna Valencia
        - Django setup, css styling, and recording button
 - Backend
    - William Morton
        - Gemini API summarization tool, and setting rules for the prompt, general bug fixing, pioneering tests 
    - Aiden Reedy 
        - Speech to text transcription optimization
 - Fullstack
    - Nadir Isweesi
        - Django setup, created API calls to different LLMS
    - Ryan Fairhurst
        - Viewing all local summaries, downloading summaries, and viewing summaries on the site, CI implemenation
    - Aidan Daly
        - Summarization integration, both implementing and linking with the backend