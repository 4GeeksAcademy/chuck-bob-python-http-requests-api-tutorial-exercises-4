import requests

# Your code here

response = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")
resp_json = response.json()

print(resp_json[1]["name"])