#HEADERS
import requests

url="https://jsonplaceholder.typicode.com/posts"

headers = {
    "Content-Type": "application/json"
}

payload ={
    "title": "This is my title",
    "body": "This is my body",
    "userId": 1
}

response = requests.post(url, headers=headers, json=payload)

content = response.json()

statusCode = response.status_code

print(statusCode)
print(content)
