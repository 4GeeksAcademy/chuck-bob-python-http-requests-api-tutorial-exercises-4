import requests

# Your code here

response = requests.post("https://assets.breatheco.de/apis/fake/sample/post.php")
resp_json = response.json()

print(resp_json)