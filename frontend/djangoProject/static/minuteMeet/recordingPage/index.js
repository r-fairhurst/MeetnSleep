// Define eventSource globally
let eventSource = null;
let transcriptText = "";

document.addEventListener("DOMContentLoaded", function () {
    const transcriptElement = document.getElementById("live-transcript");
    const startButton = document.getElementById("start-button");
    const stopButton = document.getElementById("stop-button");
    const deviceList = document.getElementById("recording-device-list");

    startButton.style.display = "inline-block";
    stopButton.style.display = "none";

    function startTranscription() {
        if (eventSource) {
            console.warn("Transcription already started!");
            return;
        }

        // Get the selected device option
        const selectedOption = deviceList.options[deviceList.selectedIndex];
        const selectedDeviceIndex = deviceList.value;
        
        if (!selectedDeviceIndex || selectedDeviceIndex === "") {
            alert("Please select a recording device first");
            return;
        }
        
        // Get device properties
        const deviceId = selectedOption.getAttribute("data-device-id");
        const isLoopback = selectedOption.getAttribute("data-loopback") === "true";
        const isGlobal = selectedOption.getAttribute("data-global") === "true";
        
        alert("Starting Transcription");
        console.log(`Starting transcription with device index: ${selectedDeviceIndex}`);
        if (isLoopback) console.log("Using desktop audio capture");
        if (isGlobal) console.log("Using global desktop audio capture");

        // Build the stream URL with appropriate parameters
        let streamUrl = `/minuteMeet/stream_transcription/?device_index=${selectedDeviceIndex}`;
        
        if (isLoopback) {
            streamUrl += `&is_loopback=true`;
        }
        
        if (isGlobal) {
            streamUrl += `&is_global=true`;
        }
        
        if (deviceId) {
            streamUrl += `&device_id=${encodeURIComponent(deviceId)}`;
        }
        
        eventSource = new EventSource(streamUrl);

        eventSource.onmessage = function (event) {
            const data = JSON.parse(event.data);
            transcriptElement.innerHTML += `<br> ${data.text}`;
            transcriptText += data.text + "\n";
        };

        eventSource.onerror = function () {
            console.warn("Error occurred, stopping transcription...");
            stopTranscription();
        };

        // Toggle button visibility
        startButton.style.display = "none"; // Hide start button
        stopButton.style.display = "inline-block"; // Show stop button
    }

    function stopTranscription() {
        if (!eventSource) {
            console.warn("No active transcription to stop.");
            return;
        }

        alert("Stopping Transcription");
        console.log("Stopping transcription...");

        fetch("/minuteMeet/stop_transcription_stream/", { method: "POST" })
            .then(response => response.json())
            .then(data => {
                console.log("Stopped:", data);
                eventSource.close();
                eventSource = null;
                downloadTranscript();
            })
            .catch(error => console.error("Error stopping:", error));

        //transcriptElement.innerHTML += "<br><span style='color:red;'>Transcription stopped</span>";

        // Toggle button visibility
        startButton.style.display = "inline-block"; // Show start button
        stopButton.style.display = "none"; // Hide stop button
    }

    function downloadTranscript() {
        const blob = new Blob([transcriptText], { type: "text/plain" });
        const link = document.createElement("a");
        link.href = URL.createObjectURL(blob);
        link.download = "transcript.txt";
        link.click();
    }

    // Attach event listeners
    startButton.addEventListener("click", startTranscription);
    stopButton.addEventListener("click", stopTranscription);
});

// Helper function to get CSRF token
function getCSRFToken() {
    return document.cookie.split("; ")
        .find(row => row.startsWith("csrftoken"))
        ?.split("=")[1];
}

window.addEventListener("beforeunload", () => {
    if (eventSource) {
        fetch("/minuteMeet/stop_transcription_stream/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken(),
            },
        }).catch(error => console.error("Error stopping transcription:", error));

        eventSource.close();
        eventSource = null;
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const deviceList = document.getElementById("recording-device-list");

    // Fetch the list of input devices
    fetch("/minuteMeet/get_input_devices/")
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Add option groups for different device types
                const globalGroup = document.createElement("optgroup");
                globalGroup.label = "Global Audio";
                
                const micGroup = document.createElement("optgroup");
                micGroup.label = "Microphones";
                
                const desktopGroup = document.createElement("optgroup");
                desktopGroup.label = "Specific Desktop Audio";
                
                data.devices.forEach(device => {
                    const option = document.createElement("option");
                    option.value = device.index;
                    option.textContent = device.name;
                    
                    // Store device attributes as data attributes
                    if (device.id) {
                        option.setAttribute("data-device-id", device.id);
                    }
                    
                    if (device.is_loopback) {
                        option.setAttribute("data-loopback", "true");
                    }
                    
                    if (device.is_global) {
                        option.setAttribute("data-global", "true");
                        globalGroup.appendChild(option);
                    } else if (device.is_virtual || device.is_loopback) {
                        desktopGroup.appendChild(option);
                    } else {
                        micGroup.appendChild(option);
                    }
                });
                
                // Add the groups to select element
                if (globalGroup.children.length > 0) {
                    deviceList.appendChild(globalGroup);
                }
                
                if (micGroup.children.length > 0) {
                    deviceList.appendChild(micGroup);
                }
                
                if (desktopGroup.children.length > 0) {
                    deviceList.appendChild(desktopGroup);
                }
            } else {
                console.error("Failed to load input devices:", data.message);
            }
        })
        .catch(error => console.error("Error fetching input devices:", error));
});
