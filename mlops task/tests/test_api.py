import requests

url = "http://localhost:8000/predict"
files = {"file": open("tests/test_api_data.csv", "rb")}
response = requests.post(url, files=files)
print(response.json())
