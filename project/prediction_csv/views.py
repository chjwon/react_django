from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import torch
import numpy as np
import joblib
from .lstm_utils import LSTMModel, hidden_size, output_size, num_layers
import json

with open("./file_path.json", 'r') as file:
    fileName = json.load(file)['prediction_csv'][0]

input_size = 5  # 'Open', 'High', 'Low', 'Close', 'Volume'

scaler = joblib.load(fileName['close_scaler'])

model = LSTMModel(input_size, hidden_size, output_size, num_layers)
model.load_state_dict(torch.load(fileName['lstm_model']))
model.eval()

def preprocess_time_series(data):
    data = np.array(data)
    data = torch.tensor(data, dtype=torch.float32).unsqueeze(0).unsqueeze(0)
    return data

class PredictStockView(APIView):
    def post(self, request):
        try:
            input_data = request.data.get('time_series_data')

            if input_data is None:
                return Response({'error': 'No data provided'}, status=status.HTTP_400_BAD_REQUEST)
            
            # preprocess
            input_tensor = preprocess_time_series(input_data)
            
            # prediction
            with torch.no_grad():
                prediction = model(input_tensor)
            
            prediction = prediction.detach().numpy()

            # inverse_transform
            prediction_original_scale = scaler.inverse_transform(prediction.reshape(-1, 1))

            return Response({'prediction': prediction_original_scale[0][0]}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
