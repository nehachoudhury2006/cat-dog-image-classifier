# Image Classifier Project

Goal: Build a CNN image classification model that predicts whether an uploaded image is a cat or dog first, then later expand to more animals.

## Phase 1: Training in Jupyter or Google Colab

Use this phase to:

- Load image dataset
- Resize and normalize images
- Train a CNN or transfer learning model
- Check accuracy
- Save the trained model in `models/`

Recommended first model:

- TensorFlow/Keras
- MobileNetV2 transfer learning
- Classes: cat, dog

## Phase 2: App in VS Code

Use this phase to:

- Load the saved model
- Build a Streamlit upload app
- Accept an image from the user
- Show prediction and confidence

## Phase 3: Cloud Deployment

Deploy only:

- App code
- Saved model file
- Requirements file

Recommended cloud option:

- Hugging Face Spaces with Streamlit

## Folder Structure

```text
image_classifier/
  dataset/
    train/
      cat/
      dog/
    test/
      cat/
      dog/
  notebooks/
  models/
  app/
```

## First Task

Add cat images into:

```text
dataset/train/cat/
dataset/test/cat/
```

Add dog images into:

```text
dataset/train/dog/
dataset/test/dog/
```

For the first version, use around 100-200 images per class. Later, increase it for better accuracy.
