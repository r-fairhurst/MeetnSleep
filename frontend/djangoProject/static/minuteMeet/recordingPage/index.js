document.addEventListener("DOMContentLoaded", function () {
    const transcriptElement = document.getElementById("live-transcript");
    let eventSource = null;

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

    // Start automatically when page loads
    startTranscription();
});


// Helper function to get CSRF token
// this will ensure Django accepts the request instead of rejecting it as a potential CSRF attack
// read more: https://portswigger.net/web-security/csrf
function getCSRFToken() {
    return document.cookie.split("; ")
        .find(row => row.startsWith("csrftoken"))
        ?.split("=")[1];
}

// this is for testing purposes
export { startTranscription, getCSRFToken };