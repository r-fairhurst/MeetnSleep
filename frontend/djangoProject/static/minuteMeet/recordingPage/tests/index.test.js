const { getCSRFToken, startTranscription } = require("../index.js");

// Mock EventSource globally
global.EventSource = jest.fn(() => {
    return {
        onmessage: jest.fn(),
        onerror: jest.fn(),
        close: jest.fn(),
    };
});

// Unit Test: Extract CSRF Token
test("getCSRFToken extracts the CSRF token from cookies", () => {
    document.cookie = "csrftoken=abc123; othercookie=value";
    const token = getCSRFToken();
    expect(token).toBe("abc123");
});

test("getCSRFToken returns undefined if no CSRF token is found", () => {
    document.cookie = "othercookie=value";
    const token = getCSRFToken();
    expect(token).toBeUndefined();
});

// Integration Test: Ensure transcript updates on message event
test("startTranscription appends received text to transcript", () => {
    document.body.innerHTML = '<div id="live-transcript"></div>';
    const eventSource = startTranscription(); // Start transcription

    // Simulate a message event
    eventSource.onmessage({ data: JSON.stringify({ text: "Hello world" }) });

    const transcriptElement = document.getElementById("live-transcript");
    expect(transcriptElement.innerHTML).toContain("Hello world");
});

// Error Handling Test: Ensure errors are handled correctly
test("startTranscription handles errors correctly", () => {
    document.body.innerHTML = '<div id="live-transcript"></div>';
    const eventSource = startTranscription(); // Start transcription

    // Simulate an error event
    eventSource.onerror();

    const transcriptElement = document.getElementById("live-transcript");
    expect(transcriptElement.innerHTML).toContain("Recording stopped");
});

// System Test: Ensure previous EventSource is closed before new one is created
test("startTranscription closes existing EventSource before creating a new one", () => {
    document.body.innerHTML = '<div id="live-transcript"></div>';
    const eventSource1 = startTranscription();
    const closeSpy = jest.spyOn(eventSource1, "close");

    const eventSource2 = startTranscription(); // Call again to trigger closure

    expect(closeSpy).toHaveBeenCalled();
});
