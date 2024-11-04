import requests

def test_prediction():
    # Test the /prediction/ endpoint with an image file
    url = 'http://localhost:8000/prediction/'
    file_path = './images.jpg'

    try:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(url, files=files)
            if response.status_code == 200:
                print("Prediction Response:", response.json())
            else:
                print(f"Prediction failed with status code {response.status_code}: {response.text}")
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred during the prediction test: {e}")

def test_prediction_csv():
    # Test the /predict_timeseries/ endpoint with sample time series data
    url = 'http://localhost:8000/predict_timeseries/'
    data = {
        'time_series_data': [40.6, 40.76, 40.31, 0, 36865322]  # Example time series data
    }

    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Prediction CSV Response:", response.json())
        else:
            print(f"Prediction CSV failed with status code {response.status_code}: {response.text}")
    except Exception as e:
        print(f"An error occurred during the prediction_csv test: {e}")

def test_gpt_response():
    # Test the /gpt/ endpoint with a text prompt
    url = 'http://localhost:8000/gpt/'
    data = {
        'text': "What is the capital of France?"
    }

    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("GPT Response:", response.json())
        else:
            print(f"GPT response failed with status code {response.status_code}: {response.text}")
    except Exception as e:
        print(f"An error occurred during the GPT response test: {e}")

if __name__ == "__main__":
    test_prediction()
    test_prediction_csv()
    test_gpt_response()
