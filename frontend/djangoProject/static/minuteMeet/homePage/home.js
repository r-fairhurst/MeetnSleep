/*************************************************
link the home page buttons to corresponding pages
*************************************************/

//home to recording
document.addEventListener("DOMContentLoaded", function() {
    let button = document.getElementById("create-button");

    if (button) {
        button.addEventListener("click", function() {
            console.log("clicked");
            window.location.href = "/minuteMeet/recordingPage/";
        });
    }
});

//home to archive
document.addEventListener("DOMContentLoaded", function() {
    let button = document.getElementById("archive-button");

    if (button) {
        button.addEventListener("click", function() {
            console.log("clicked");
            window.location.href = "/minuteMeet/archivePage/";
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