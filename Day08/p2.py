import requests

#TO CREATE THE DATA
'''''
url="https://jsonplaceholder.typicode.com/posts"

data={"title":"this is my title",
      "body":"this is my body",
      "userid":1}

response = requests.post(url,json = data)  
content = response.json()# get the requests from that url

print("status code:",response.status_code) # status of that code
print("response body:",content) # print the contents'''

# TO PATCH THE VALUE

url="https://jsonplaceholder.typicode.com/posts/100"

data={"title":"this is my title"}

response = requests.patch(url,json = data)# get the requests from that url
content = response.json() # getting the data from that url

print("status code:",response.status_code) # status of that code
print("response body:",content) # print the contents
