import requests

def test_prediction():
    url = 'http://localhost:8000/prediction/'
    file_path = './images.jpg'

    try:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(url, files=files)
            assert response.status_code == 200, f"Prediction failed with status code {response.status_code}: {response.text}"
            response_data = response.json()
            assert "prediction" in response_data, "Key 'prediction' not found in the response"
            print("Prediction test passed:", response_data)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except AssertionError as e:
        print(f"Assertion error in prediction test: {e}")
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
        assert response.status_code == 200, f"Prediction CSV failed with status code {response.status_code}: {response.text}"
        response_data = response.json()
        assert "prediction" in response_data, "Key 'prediction' not found in the response"
        print("Prediction CSV test passed:", response_data)
    except AssertionError as e:
        print(f"Assertion error in prediction CSV test: {e}")
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
        assert response.status_code == 200, f"GPT response failed with status code {response.status_code}: {response.text}"
        response_data = response.json()
        assert "response" in response_data, "Key 'response' not found in the response"
        print("GPT response test passed:", response_data)
    except AssertionError as e:
        print(f"Assertion error in GPT response test: {e}")
    except Exception as e:
        print(f"An error occurred during the GPT response test: {e}")

if __name__ == "__main__":
    test_prediction()
    test_prediction_csv()
    test_gpt_response()
