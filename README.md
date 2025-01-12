# MeetnSleep

## Project Proposal - Team 10

### Team Information

| Name             | Role                           | Responsibility                                      |
|------------------|--------------------------------|-----------------------------------------------------|
| Ian McKee        | Team Leader / Software Testing | Facilitate project, Instructor communication        |
| William Morton   | Backend Engineer               | Help develop the backend portion of the software    |
| Aidan Daly       | Software Tester                | Help test the backend/front-end side of the project |
| Ryan Fairhurst   | Front End Engineer             | GitHub repo owner and help with the UI design       |
| Arianna Valencia | Front End Engineer             | Help develop front-end of the project               |
| Aiden Reedy      | Backend Engineer               | Help develop the backend portion of the software    |
| Nadir Isweesi    | Full Stack Engineer            | Help design the backend and the front end of the project |


### GitHub Repo:
https://github.com/r-fairhurst/MeetnSleep 

### Communication channels:
- Discord (primary)
- Email (backup)
- GitHub

### Rules For communication
- Be respectful when communicating with other team members.
- Communicate issues early.
- Respond to messages within 24 hours. (excluding holidays)
- If you cannot attend a meeting, 

## Product description 

### Team Names: 
Ian McKee, William Morton, Aidan Daly, Ryan Fairhurst, Arianna Valencia, Aiden Reedy, Nadir Isweesi

### Abstract: 
Our product is a meeting summary tool that the user can boot up to listen to a specific program's audio output and then go do something else. When the meeting is over and the User can stop recording, the program will then summarize the meeting, provide all the essential details, and give a broad overview of the entire meeting. 

### Goal: 
This product aims to streamline the process of taking meeting notes and allow customers to increase their productivity even on platforms that don’t natively support.
Novelty:

Our approach to this meeting summary will be to condense meetings into shortened main points, instead of just recording audio and converting it to text. We will also summarize it for you. The main draw for our product is that it can be used in real life and with multiple different meeting software, making it accessible regardless of the environment.

### Effects: 
Our product will streamline the note-taking process and automatically record the minutes of each meeting. This will boost customer productivity by allowing meeting participants to focus on the actual content of the meeting rather than recording it. 

### Technical approach: 
We plan to use Python as the main language and create a Desktop App where the user can input a program/source to listen to. 
Multiple speech-to-text libraries exist that we can use for our own project. We can make an API call to some LLM to help summarize the full meeting. 

### Risks/Potential Issues:
Figuring out how to accurately convert speech into text using different inputs and gathering this speech from either a microphone or a program such as Discord/Microsoft Teams could create issues.

We risk missing content if we summarize the meeting too much. Customers wouldn’t like missing important details.

### Current Practice: 
Currently, Microsoft Teams and Zoom both have a feature that is very similar to this, however they only support meeting transcripts and are both limited by being proprietary software. 
This application would be beneficial because it would be compatible with various different platforms and would provide the added feature of summarizing and condensing meeting content. 

## Product Features:

### Major Features:
- Translate audio into text.
- Summarize the conversation.
- Provide the full transcript of the meeting to the user.
- Save the conversation/summary to the user’s computer.
- Be able to get audio input from multiple different sources. (e.g., real-life microphone, Discord, Microsoft Teams, Zoom, etc.)

### Stretch Goals:
- Support different languages
- Create a web application
- User accounts
- Cloud support (Storage, Access Anywhere)
