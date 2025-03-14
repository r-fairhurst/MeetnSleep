
// Lol simple back button logic
document.addEventListener("DOMContentLoaded", function() {
    let backButton = document.getElementById("back-button");

    if (backButton) {
        backButton.addEventListener("click", function() {
            console.log("back clicked");
            window.location.href = "/minuteMeet/summaryPage/";
        });
    }
});