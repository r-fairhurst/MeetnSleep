# Changelog

All important changes to this project will be documented in this file.

## [Unreleased]
- use it for upcoming changes

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
