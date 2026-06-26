# Cat vs Dog Image Classifier

Live App: https://cat-dog-image-classifier-gyfvgiwhsnsc8p88fwgzfu.streamlit.app/

## Objective

This project is a deep learning image classification app that predicts whether an uploaded image is a cat or a dog.

## Technologies Used

- Python
- TensorFlow/Keras
- Streamlit
- NumPy
- Pillow

## How It Works

1. The user uploads a cat or dog image in the Streamlit app.
2. The app resizes the image to `128x128`.
3. The image is normalized so pixel values are between `0` and `1`.
4. The trained CNN model predicts the class.
5. The app displays the prediction and confidence score.

## Model

The project uses a CNN model saved in Keras format:

```text
models/cat_dog_custom_cnn.keras
```

This is a supervised deep learning model for binary image classification.

## Run Locally

```bash
cd /Users/nehachoudhury/image_classifier
source .venv/bin/activate
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

## Cloud Deployment

The app is deployed on Streamlit Cloud. Streamlit Cloud reads:

- `runtime.txt` for the Python version
- `requirements.txt` for required libraries
- `app.py` as the main app file

`runtime.txt` uses Python 3.11 because TensorFlow works reliably with that version.

## Future Improvements

- Train the model with a larger dataset
- Add more animal classes
- Improve model accuracy
- Add prediction history
- Add a more detailed result explanation
