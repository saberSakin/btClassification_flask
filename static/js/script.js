document.getElementById("upload-form").addEventListener("submit", function (e) {
  e.preventDefault();

  const imageInput = document.getElementById("image-input");
  const uploadedImage = document.getElementById("uploaded-image");
  const resultDiv = document.getElementById("result");
  const uploadingMessage = document.getElementById("uploading-message");

  const formData = new FormData();
  formData.append("image", imageInput.files[0]);

  //////// Display the uploading message
  uploadingMessage.style.display = "block";

  fetch("/predict", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      resultDiv.innerText = `Predicted Class: ${data.prediction}`;
      uploadedImage.src = URL.createObjectURL(imageInput.files[0]);
      /// Hide the uploading message
      uploadingMessage.style.display = "none";
      /// Display the uploaded image
      uploadedImage.style.display = "block";
    })
    .catch((error) => {
      console.error("Error:", error);
      /// Hide the uploading message in case of an error
      uploadingMessage.style.display = "none";
    });
});
