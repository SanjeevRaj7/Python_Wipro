#USING GET METHOD
import requests

'''''
url="https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url) # get the requests from that url

print("status code:",response.status_code) # status of that code
print("response body:",response.json()) # print the contents '''

'''''
url="https://sbi.co.in"
response = requests.get(url) 
content = response.content 
print("status:",response.status_code) 
print("response body:",content) '''

url="https://jsonplaceholder.typicode.com/posts/101"

response = requests.get(url)
content = response.json()# get the requests from that url

print("status code:",response.status_code) # status of that code
print("response body:",content) # print the contents
