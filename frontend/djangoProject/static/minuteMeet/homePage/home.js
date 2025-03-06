/*************************************************
link the home page buttons to corresponding pages
*************************************************/

//home to recording
document.addEventListener("DOMContentLoaded", function() {
    let createButton = document.getElementById("create-button");

    if (createButton) {
        createButton.addEventListener("click", function() {
            console.log("create clicked");
            window.location.href = "/minuteMeet/recordingPage/";
        });
    }

    let settingsButton = document.getElementById("settings-button");

    if (settingsButton) {
        settingsButton.addEventListener("click", function() {
            console.log("settings clicked");
            window.location.href = "/minuteMeet/settingsPage/";
        });
    }

    let summaryButton = document.getElementById("summary-button");

    if (summaryButton) {
        summaryButton.addEventListener("click", function() {
            console.log("summary clicked");
            window.location.href = "/minuteMeet/summaryPage/";
        });
    }
});


/*************************************************
file upload functionality
*************************************************/

document.getElementById("uploadForm").addEventListener("submit", function(event) {
    event.preventDefault();
    let fileInput = document.getElementById("audioFile");
    if (!fileInput.files.length) {
        alert("Please select an audio file.");
        return;
    }

    let formData = new FormData();
    formData.append("audio_file", fileInput.files[0]);

    fetch("/upload_audio_transcription/", {
        method: "POST",
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Transcript: " + data.transcript);
        } else {
            alert("Could not process the audio file.");
        }
    })
    .catch(error => console.error("Error:", error));
});