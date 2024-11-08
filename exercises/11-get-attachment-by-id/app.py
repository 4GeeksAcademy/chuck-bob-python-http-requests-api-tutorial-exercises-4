import requests

def get_attachment_by_id(attachment_id):
    # Your code here
    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    resp_json = response.json()

    for post in resp_json['posts']:
        for attachment in post['attachments']:
            if attachment['id'] == attachment_id:
                return attachment

print(get_attachment_by_id(137))