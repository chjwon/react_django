# Time Series Prediction API

## Overview
This project provides an API for predicting stock prices using a time series dataset. It utilizes a Long Short-Term Memory (LSTM) model to forecast future stock prices based on historical data such as 'Open', 'High', 'Low', 'Close', and 'Volume'. The project is built using Django and integrates a pretrained LSTM model for predictions.

## Dataset

We use the **Microsoft Stock Time Series Dataset** from Kaggle as a sample for training and testing the model:

[Kaggle Dataset - Microsoft Stock Time Series Analysis](https://www.kaggle.com/datasets/vijayvvenkitesh/microsoft-stock-time-series-analysis)

The dataset contains historical stock data such as open, close, high, low prices, and volume for Microsoft (MSFT).

## Project Structure

- **`manage.py`**: Main Django project management file.
- **`file_path.json`**: Stores file paths for pretrained models, scalers, and the stock dataset.
- **`lstm_train.py`**: Script for training the LSTM model on the time series dataset(currently requires optimization due to overfitting).
- **`lstm_utils.py`**: Contains the LSTM model class definition and configuration (e.g., hidden size, output size, number of layers).
- **`views.py`**: Contains the `PredictStockView` class for handling the prediction API requests.
- **`file_path.json`**: Configuration file holding paths to the scaler and pretrained LSTM model.
