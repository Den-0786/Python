import requests

PARAMETERS = {
    "amount": 20,
    "type":"boolean",
    "category": 18
}

response = requests.get("https://opentdb.com/api.php", params=PARAMETERS)
response.raise_for_status()
data = response.json()
question_data = data["results"]