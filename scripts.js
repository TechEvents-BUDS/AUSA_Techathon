function submitSymptoms() {
    const symptoms = document.getElementById('symptoms').value;

    if (!symptoms) {
        alert("Please enter your symptoms!");
        return;
    }

    // Send symptoms to Flask backend
    fetch('/analyze_symptoms', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ symptoms: symptoms })
    })
    .then(response => response.json())
    .then(data => {
        // Display the advice and doctor recommendation
        if (data.advice) {
            document.getElementById('advice').innerText = "Advice: " + data.advice;
        } else if (data.error) {
            document.getElementById('advice').innerText = "Error: " + data.error;
        }
    })
    .catch(error => {
        document.getElementById('advice').innerText = "An error occurred: " + error;
    });
}