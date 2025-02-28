// Define eventSource globally
let eventSource = null;

document.addEventListener("DOMContentLoaded", function () {
    const transcriptElement = document.getElementById("live-transcript");
    let eventSource;

    function startTranscription() {
        if (eventSource) {
            eventSource.close();
        }

        // Open a connection to Django streaming endpoint
        eventSource = new EventSource("/minuteMeet/stream_transcription/");

        eventSource.onmessage = function (event) {
            const data = JSON.parse(event.data);
            transcriptElement.innerHTML += `<br> ${data.text}`;
        };

        eventSource.onerror = function () {
            transcriptElement.innerHTML += "<br><span style='color:red;'>Recording stopped</span>";
            eventSource.close();
        };
    }

    const startRecordingButton = document.getElementById("start-button");

    startRecordingButton.addEventListener("click", function() { 
        console.error("Transcription starting");
        startTranscription();
    });
});

function stopTranscription() {
    const stopRecordingButton = document.getElementById("stop-button");
    if (!stopRecordingButton) {
        console.error("Stop button not found");
        return;
    }
    
    // Add event listener to the stop button
    stopRecordingButton.addEventListener("click", function() {
        console.log("Stop button clicked!");
        
        // Close the event source first
        if (eventSource) {
            eventSource.close();
            eventSource = null;
        }
        
        eventSource = new EventSource("/minuteMeet/stop_transcription/");
        eventSource.onmessage = function(event) {
            console.log("Transcription stopped");
            eventSource.close();
            eventSource = null;
        };

        eventSource.onerror = function() {
            console.error("Error stopping transcription");
            eventSource.close();
            eventSource = null;
        }
        
    });
}

// Call the function when DOM is loaded to attach the event listener
document.addEventListener("DOMContentLoaded", function() {
    stopTranscription();
});


// Helper function to get CSRF token
// this will ensure Django accepts the request instead of rejecting it as a potential CSRF attack
// read more: https://portswigger.net/web-security/csrf
function getCSRFToken() {
    return document.cookie.split("; ")
        .find(row => row.startsWith("csrftoken"))
        ?.split("=")[1];
}