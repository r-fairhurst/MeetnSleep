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


document.addEventListener("DOMContentLoaded", () => {
    const startButton = document.getElementById("create-button");

    startButton.addEventListener("click", () => {
        fetch("/start_transcription/", {
            method: "POST",
            headers: {
                "X-CSRFToken": getCSRFToken(),
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert("Transcript: " + data.transcript);
            } else {
                alert("Speech not recognized. Try again.");
            }
        })
        .catch(error => console.error("Error:", error));
    });
});

// Helper function to get CSRF token
// this will ensure Django accepts the request instead of rejecting it as a potential CSRF attack
// read more: https://portswigger.net/web-security/csrf
function getCSRFToken() {
    return document.cookie.split("; ")
        .find(row => row.startsWith("csrftoken"))
        ?.split("=")[1];
}
