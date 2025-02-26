function startTranscription() {
    const transcriptElement = document.getElementById("live-transcript");
    let eventSource = new EventSource("/minuteMeet/stream_transcription/");

    eventSource.onmessage = function (event) {
        const data = JSON.parse(event.data);
        transcriptElement.innerHTML += `<br> ${data.text}`;
    };

    eventSource.onerror = function () {
        transcriptElement.innerHTML += "<br><span style='color:red;'>Recording stopped</span>";
        eventSource.close();
    };

    return eventSource; // Returning for testability
}

// Helper function to get CSRF token
function getCSRFToken() {
    return document.cookie.split("; ")
        .find(row => row.startsWith("csrftoken"))
        ?.split("=")[1];
}

// Ensure function is called when the page loads
document.addEventListener("DOMContentLoaded", startTranscription);

// Export functions for testing
module.exports = { startTranscription, getCSRFToken };