from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import cv2
import numpy as np

app = Flask(__name__)

# model load
model = tf.keras.models.load_model("model.h5")


# upload img function
def preprocess_image(image_path):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(150, 150))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.keras.applications.efficientnet.preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"})

    image = request.files["image"]
    image_path = "temp.jpg"
    image.save(image_path)
    processed_image = preprocess_image(image_path)

    # Make predictions
    prediction = model.predict(processed_image)
    class_index = np.argmax(prediction)

    # Swap class labels for "pituitary" and "notumor"
    class_labels = ["glioma", "meningioma", "pituitary", "notumor"]
    if class_labels[class_index] == "pituitary":
        predicted_class = "notumor"
    elif class_labels[class_index] == "notumor":
        predicted_class = "pituitary"
    else:
        predicted_class = class_labels[class_index]

    return jsonify({"prediction": predicted_class})


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")

# ///
