// Define eventSource globally
let eventSource = null;

document.addEventListener("DOMContentLoaded", function () {
    const transcriptElement = document.getElementById("live-transcript");
    const startRecordingButton = document.getElementById("start-button");
    const stopRecordingButton = document.getElementById("stop-button");

    function startTranscription() {
        // Prevent retriggering
        if (eventSource) {
            console.warn("Transcription already started!");
            return;
        }

        alert("Starting Transcription");
        console.log("Starting transcription...");
        eventSource = new EventSource("/minuteMeet/stream_transcription/");

        eventSource.onmessage = function (event) {
            const data = JSON.parse(event.data);
            transcriptElement.innerHTML += `<br> ${data.text}`;
        };

        eventSource.onerror = function () {
            console.warn("Error occurred, stopping transcription...");
            stopTranscription();
        };

        // Disable start button, enable stop button
        startRecordingButton.disabled = true;
        stopRecordingButton.disabled = false;
    }

    function stopTranscription() {
        if (!eventSource) {
            console.warn("No active transcription to stop.");
            return;
        }

        alert("Stopping Transcription");
        console.log("Stopping transcription...");

        // Send a request to stop transcription on the server
        fetch("/minuteMeet/stop_transcription_stream/", { method: "POST" })
            .then(response => response.json())
            .then(data => {
                console.log("Stopped:", data);
                eventSource.close();
                eventSource = null;
            })
            .catch(error => console.error("Error stopping:", error));

        // Update UI
        transcriptElement.innerHTML += "<br><span style='color:red;'>Transcription stopped</span>";

        // Enable start button, disable stop button
        startRecordingButton.disabled = false;
        stopRecordingButton.disabled = true;
    }

    // Attach event listeners once
    startRecordingButton.addEventListener("click", startTranscription);
    stopRecordingButton.addEventListener("click", stopTranscription);
});

// Helper function to get CSRF token
function getCSRFToken() {
    return document.cookie.split("; ")
        .find(row => row.startsWith("csrftoken"))
        ?.split("=")[1];
}