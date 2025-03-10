# 1. How to install the software

### Prerequisites
- Python >= 3.10
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

# 2. How to run the software.
To run the program, you will need to run the following command in the terminal.

```bash
python frontend/djangoProject/manage.py runserver
```

this should initiallize a local server that you can access by going to the following link in your browser.

# 3. How to use the software

This software is designed for users who are familiar with our platform

**Web Application (work in progress)**

- Open your preferred web browser.

- Navigate to the localhost URL provided

```
http://127.0.0.1:8000/minuteMeet
```

# 4. Support & Questions

### Found a bug?
If you ever encounter a bug while using our software and want to help us keep our product bug-free then follow these guidelines!

#### Step 1
If you found a bug, make sure you are using the latest software version we have available, and also double check that it is not already listed within the issue tracker found on github: https://github.com/r-fairhurst/MeetnSleep/issues 
- **NOTE:** If you do not have an account on GitHub and do not wish to create one you can email one the devs about the bug following the same format.

#### Step 2
Figure out the steps to reproduce the bug
- this is most useful if the steps are specific and anyone could follow them to reproduce the bug

#### Step 3
Follwing our bug report template found in this folder named "bug_report_template", a new issue can be created on our github found here: https://github.com/r-fairhurst/MeetnSleep/issues 
- **NOTE:** If you do not have an account on GitHub and do not wish to create one you can email one the devs about the bug following the same format. 

#### Step 4
Simply wait for us to fix it, and keep an ear out if we need any more information from you

- Reach out to the maintainers via isweesin@oregonstate.edu or mortonwi@oregonstate.edu

# 5. Known bugs

- take a look at our github issues to see if the bug you are experiencing is already listed there
- https://github.com/r-fairhurst/MeetnSleep/issues 
