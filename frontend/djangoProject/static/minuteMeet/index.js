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

