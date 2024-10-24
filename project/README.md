# REACT_Django

## Overview
This project uses machine learning models to make predictions, including stock price forecasting using LSTM models. It is built with Django and provides an AI-powered API for prediction tasks.

## Project Structure

- `manage.py`: Main Django project file.
- `file_path.json`: Contains file paths to pretrained models, scalers, and training datasets required for predictions.

## File: `file_path.json`
This file is located in the same directory as `manage.py` and holds the necessary paths for the project to function properly. It follows the format below:

```json
{
    "prediction_csv": [{
        "close_scaler": "somepath/close_scaler.pkl",
        "lstm_model": "somepath/lstm_stock_model.pth",
        "ms_stock_file": "somepath/Microsoft_Stock.csv"
    }],
    "prediction": [{}],
    "app": [{}]
}
```