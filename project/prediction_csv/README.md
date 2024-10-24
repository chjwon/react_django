# Time Series Prediction API

## Overview
This project provides an API for predicting stock prices using a time series dataset. It utilizes Long Short-Term Memory (LSTM) models to forecast future stock prices based on historical data. The project is built using Django and a pretrained LSTM model for predictions.

## Dataset

We use the **Microsoft Stock Time Series Dataset** from Kaggle as a sample for training and testing the model:

[Kaggle Dataset - Microsoft Stock Time Series Analysis](https://www.kaggle.com/datasets/vijayvvenkitesh/microsoft-stock-time-series-analysis)

The dataset contains historical stock data such as open, close, high, low prices, and volume for Microsoft (MSFT).

## Project Structure

- **`manage.py`**: Main Django project management file.
- **`file_path.json`**: Stores file paths for pretrained models, scalers, and the stock dataset.
- **`lstm_train.py`**: Script for training the LSTM model on the time series dataset (currently requires optimization due to overfitting).

