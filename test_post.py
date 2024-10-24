import requests

# test prediction - post function
url = 'http://localhost:8000/prediction/'

file_path = './images.jpg'

with open(file_path, 'rb') as f:
    files = {'file': f}

    response = requests.post(url, files=files)

    print(response.json())

# test prediction_csv - post function
url = 'http://localhost:8000/predict_timeseries/'
data = {
    'time_series_data': [40.6,40.76,40.31,0,36865322]  # 예시 시계열 데이터
}

response = requests.post(url, json=data)
print(response.json())