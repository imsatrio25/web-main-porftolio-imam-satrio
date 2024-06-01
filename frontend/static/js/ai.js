//--------------------HANDLE FORM-------------------\\
const predictionContainer = document.getElementById('prediction-container');

// Handle form submission (assuming Django form rendering)
const form = document.querySelector('form'); // Select the form element

form.addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent default form submission behavior

  fetch('{% url `upload_image` %}', { // Replace with your actual view URL
    method: 'POST',
    body: new FormData(form) // Extract form data using the selected form
  })
  .then(response => response.json()) // Parse JSON response from the view
  .then(data => {
    if (data.prediction && data.predicted_image_url) { // Check for response data
      predictionContainer.style.display = 'block'; // Show prediction container
      document.getElementById('prediction').textContent = data.prediction;
      document.getElementById('predicted-image').src = data.predicted_image_url;
    } else {
      // Handle any errors or empty response
    }
  })
  .catch(error => console.error(error)); // Handle errors during fetch
});


function tryAnotherPrediction() {
    document.getElementById("prediction-container").style.display = "block";
    // This line is commented out as Django might not assign "upload-form" as the ID
    // document.getElementById("upload-form").style.display = "block"; 
    document.querySelector('form').reset(); // Reset the form using the selected form element
}
