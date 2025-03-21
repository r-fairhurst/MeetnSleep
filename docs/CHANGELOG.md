# Changelog

All important changes to this project will be documented in this file.

## [Unreleased]
- use it for upcoming changes
  
## [1.0.5] - 2024-03-06-2025 
### Added
- Made the header into a home button

### Changed
- Changed speech_recognition_service.py to use threads for recording
- header.html to add button
- recordingPage/index.js to stop recording when page unloads

## [1.0.4] - 2024-03-05-2025 [16:46]
### Added
- Added audio file upload for transcription.
- Added the ability to download the file as a .txt file that can be summarized.

### Changed
- Modified home.js and views.py.
- Changed the file transcription to download the transcript instead of just showing it to the user.

### Fixed
- Fixed the upload audio file transcription.

## [1.0.3] - 2024-03-05-2025 [16:46]
### Added
- Added notifications for starting and stopping transcription.

### Changed
- Modified recording.html, recording.css, index.js.
- Changed the recording button so that it toggles between the two, instead of just one button.

## [1.0.2] - 2024-03-2-2025 [20:07]
### Added
- Added Ability to upload transcripts for summarization
- Added table to view stored summaries
- Added download functionality for summaries
- 

### Changed
- Modified urls.py, views.py, summarization.py, summary.html, summary.css
- Used api calls through views.py->summarization.py->gemini_api.py 

## [1.0.1] - 2025-02-28 [11:33]
### Added
- Added URL path for stop_transcription_stream.
- Added stop_transcription_stream to prevent the backend from transcribing when the user presses the stop button.
- Added global flag within views.py to aid with the termination of the transcription data stream.

### Changed
- Modified urls.py, views.py, and index.js for recording.
- Combined startTranscription and stopTranscription into the same function in index.js.
- Used stop_recording() and start_recording() to set the proper flags in the backend transcription service.

### Fixed
- Fixed issue regarding the stopping and starting of the transcription service.
- Improved error handling for the recording page.

## [1.0.0] - 2025-02-28
### Added
- `CHANGELOG.md` file to track any changes

### Changed
- (to list any changes in the future)

### Fixed
- (to list any fixed bugs here)
