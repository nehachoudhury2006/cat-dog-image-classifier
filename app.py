import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image


MODEL_PATH = "models/cat_dog_custom_cnn.keras"
CLASS_NAMES = ["Cat", "Dog"]
IMAGE_SIZE = (128, 128)


st.set_page_config(
    page_title="Cat vs Dog Classifier",
    page_icon="🐾",
    layout="centered",
)


@st.cache_resource
def load_cnn_model():
    return tf.keras.models.load_model(MODEL_PATH)


def prepare_image(uploaded_image):
    image = Image.open(uploaded_image).convert("RGB")
    image = image.resize(IMAGE_SIZE)
    image_array = np.array(image, dtype=np.float32) / 255.0
    return np.expand_dims(image_array, axis=0)


st.title("Cat vs Dog Image Classifier")
st.write("Upload a cat or dog image and the model will predict the class with confidence.")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"],
)

if uploaded_file is None:
    st.info("Please upload a JPG, JPEG, or PNG image to start prediction.")
else:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    try:
        with st.spinner("Analyzing image..."):
            model = load_cnn_model()
            image_batch = prepare_image(uploaded_file)
            prediction = float(model.predict(image_batch, verbose=0)[0][0])

        class_index = 1 if prediction >= 0.5 else 0
        confidence = prediction if class_index == 1 else 1 - prediction
        predicted_class = CLASS_NAMES[class_index]

        st.success(f"Prediction: {predicted_class}")
        st.metric("Confidence", f"{confidence * 100:.2f}%")
        st.progress(confidence)

        st.caption(
            "Note: This model is trained only for cat and dog images. "
            "For other animals or unclear images, prediction may be inaccurate."
        )

    except Exception as error:
        st.error("Something went wrong while making the prediction.")
        st.write(error)