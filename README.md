# MeetnSleep / Minute-Meet
Our product is a meeting summary tool that the user can boot up to listen to a specific program's audio output. The program will listen to the users microphone and or meeting software, transcribe the meeting. When the meeting is over the transcript will then save, allowing the user to submit it for summerization.

## Installation Steps

### Prerequisites
- Python 3.10
- Pip
- Git

### Cloning the Repository and installing the required packages
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

```
python -m venv "venv"
```

then activate the virtual environment

```
source venv/bin/activate
```

you can replace venv with any name you want to give the virtual environment.

then run the commands above to install all the required packages.

## Running the Program

To run the program, you will need to run the following command in the terminal.

```bash
python frontend/djangoProject/manage.py runserver
```

this should initiallize a local server that you can access by going to the following link in your browser.

```
http://127.0.0.1:8000/minuteMeet
```

make sure you go to /minuteMeet to access the main page.

## How to use the program

**NOTE** while on the site if you are the main page "http://127.0.0.1:8000/ and get a 404 error, make sure you go to the /minuteMeet page. 
- so the full link should be http://127.0.0.1:8000/minuteMeet

### Start a meeting to record
- To start a meeting, click on the "Start Meeting" button, this is the green cirlce with a + in the middle. This will have you go to the recording page
- On the recording page, you can start recording by clicking the "Start Recording" button. This will start the recording process.
- Once you are done recording, click the "Stop Recording" button to stop the recording process. this is the red square button.
- the transcript will be saved and you can submit it for summerization.
   - this file is found in the main directory of the project, in the "storage/transcripts" folder. it will be a .srt file


### submit a transcript for summerization
**NOTE** you will need a gemini API key to submit a transcript for summerization. You can get one by going to the following link and signing up for an account.
```
https://ai.google.dev/gemini-api/docs/api-key
```

this key will need to be put in KEY.env in the  directory "src/main/llms" of the project. The key should be put in the following format.

you can make this file by running the following command in the terminal.

```bash
touch src/main/llms/KEY.env
```

and then pasting in your key using echo

```bash
echo "GEMINI_KEY=YOUR KEY" > src/main/llms/KEY.env
```

the file should look like this:

```
GEMINI_KEY=YOUR_API_KEY
```

no quotes are needed around the key.

the file should now be at path "src/main/llms/KEY.env"

- To submit a transcript for summerization, click on the "Summaries" button from the main page. This will take you to the summerization page.
- On the summerization page, you can submit a transcript by clicking the "Upload & Summerize" button. This will take you to the submit transcript page.
    - Currently the only way to submit a transcript is by uploading a .srt file. You can do this by clicking the "Choose File" button and selecting the file you want to upload. it has to be a .srt file that it will look for

- once sumitted wait until you see "success: true" on the page
- you can now go back on the page and refresh to see the transcript appear
- then you can either view or download it

### Submitting a audio file for Transcription
- to submit an audio file for summerization, click browse button next to "No file selected" and select the audio file you want to submit.
- then click the "Upload & Transcribe" button to submit the audio file for summerization.


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

## Techinal Details

### Version Control
- We used Git for version control, making new branches to test new features and then merging them into the main branch when they were ready.

### Bug Tracking
- We decided to use Github issues to track bugs and features that needed to be implemented/fixed.

### Testing
- Since we use python and django for the majority of our project we implemented unit tests to test the functionality of our code. This is accomplished by using pytest and the django testing framework.

### Continuous Integration
- We used Github Actions to implement continuous integration. This allowed us to run our tests every time we pushed to the main branch. and ensure that the build was passing.

## More Information
More information can be found in the docs folder of the project. This includes the project proposal, bug reporting documentation, as well as developer guidelines.

## Contributors
 Ryan Fairhurst, William Morton, Ian McKee, Nadir Isweesi, Arianna Valencia, Aidan Daly, Aiden Reedy 

