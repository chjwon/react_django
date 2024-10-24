# Image Classification API

## Overview
This project provides an API for image classification using a pretrained ResNet-18 model from PyTorch. The API accepts image uploads via a POST request and returns the predicted class label. It is built using Django and Django REST framework.

## Project Structure

- **`manage.py`**: Main Django project file.
- **`views.py`**: Contains the logic for the `PredictView` API endpoint.
- **`requirements.txt`**: Lists all dependencies needed for the project (including `torch`, `torchvision`, `Pillow`, `djangorestframework`).

## API Endpoints

### 1. **`/api/predict/`** (POST)
This endpoint accepts an image file and returns a prediction based on the ResNet-18 model.

### Example Request (POST):
- Endpoint: `/api/predict/`
- Form-data: 
  - Key: `file`
  - Value: An image file (e.g., JPG, PNG).

```bash
curl -X POST -F "file=@path_to_image.jpg" http://localhost:8000/api/predict/
```