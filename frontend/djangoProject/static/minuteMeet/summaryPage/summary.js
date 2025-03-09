document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('summary-upload-form').addEventListener('submit', function(event) {
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
                window.location.href = '/minuteMeet/summaryPage';
            } else {
                alert(data.message || 'An error occurred while summarizing the transcript.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while summarizing the transcript.');
        });
    });
});