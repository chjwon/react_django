import requests

# test prediction - post function
url = 'http://localhost:8000/prediction/'

file_path = './images.jpg'

with open(file_path, 'rb') as f:
    files = {'file': f}

    response = requests.post(url, files=files)

    print(response.json())
