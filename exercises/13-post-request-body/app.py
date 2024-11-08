import requests



headers = { 
    "Content-Type": "application/json"
}

body = {
    "id": 2323,
    "title": "Very big project"
}

response = requests.post(
    "https://assets.breatheco.de/apis/fake/sample/save-project-json.php", headers=headers, json=body)


print(response.text)
