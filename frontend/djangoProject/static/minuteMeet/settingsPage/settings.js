/*************************************************
setting javascript file
*************************************************/

// this will handle the key upload form submission
document.addEventListener('DOMContentLoaded', function() {
    // Handle key upload form submission
    document.getElementById('settings-key-upload-form').addEventListener('submit', function(event) {
        event.preventDefault();
        var formData = new FormData(this);

        fetch(this.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                window.location.href = '/minuteMeet/';
            } else {
                alert(data.message || 'An error occurred while submitting the API key.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while submitting the API key.');
        });
    });
});