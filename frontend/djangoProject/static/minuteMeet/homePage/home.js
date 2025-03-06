/*************************************************
link the home page buttons to corresponding pages
*************************************************/

//home to recording
document.addEventListener("DOMContentLoaded", function() {
    let createButton = document.getElementById("create-button");

    //for upload pop-up toggle 
    let uploadForm = document.getElementById("uploadForm");
    let uploadButton = document.getElementById("upload-audio-button");

    // set invisible initially
    uploadForm.style.display = "none";

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

    if (uploadButton) {
        uploadButton.addEventListener("click", function() {
            console.log("upload clicked");
            uploadForm.style.display = "flex";
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

    let file = fileInput.files[0];

    const validFileTypes = ["audio/mpeg", "audio/wav", "audio/ogg", "audio/mp3"];
    if (!validFileTypes.includes(file.type)) {
        alert("Invalid file type. Please upload a valid audio file.");
        return;
    }

    alert("Transcribing audio file... \n\nPlease do not navigate away from this page until your transcript has downloaded.");
    let formData = new FormData();
    formData.append("audio_file", file);

    fetch("/minuteMeet/upload_audio_transcription/", {
        method: "POST",
        body: formData,
    })
    .then(response => response.blob())
    .then(blob => {
        const link = document.createElement("a");
        link.href = URL.createObjectURL(blob);
        link.download = "transcript.txt";
        link.click();
    })
    .catch(error => console.error("Error:", error));
});