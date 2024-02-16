import os
import requests

url = 'https://api.notion.com/v1/users'
token = os.environ["NOTION_TOKEN"]
headers = {
    "Authorization": f"Bearer {token}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

response = requests.get(url=url, headers=headers)
print(response.text)
