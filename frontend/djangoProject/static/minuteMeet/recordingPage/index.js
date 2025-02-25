document.addEventListener("DOMContentLoaded", function () {
    const startButton = document.getElementById("start-recording");
    const stopButton = document.getElementById("stop-recording");
    const transcriptElement = document.getElementById("live-transcript");
    let eventSource = null;

    startButton.addEventListener("click", function () {
        if (eventSource) {
            eventSource.close();
        }

        eventSource = new EventSource("/minuteMeet/stream_transcription/");

        eventSource.onmessage = function (event) {
            const data = JSON.parse(event.data);
            transcriptElement.innerHTML += `<br> ${data.text}`;
        };

        eventSource.onerror = function () {
            transcriptElement.innerHTML += "<br><span style='color:red;'>[Connection lost]</span>";
            eventSource.close();
        };
    });

    stopButton.addEventListener("click", function () {
        if (eventSource) {
            eventSource.close();
            eventSource = null;
            transcriptElement.innerHTML += "<br><span style='color:blue;'>[Recording Stopped]</span>";
        }
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
