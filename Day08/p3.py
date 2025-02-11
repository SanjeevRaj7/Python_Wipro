#USING IF
import requests

url="https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url) # get the requests from that url
content = response.json()

print("status code:",response.status_code) # status of that code
#print("response body:",response.json()) # print the contents

if response.status_code == 200:
    print("rsponse body:",response.json())
    data=response.json()
    print("title:",data['title'])
    print("message:",data['body'])
else:
    print("error code:",response.status_code)