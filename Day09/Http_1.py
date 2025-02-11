import http.client

con = http.client.HTTPSConnection("jsonplaceholder.typicode.com") # connect to url using http

con.request('GET','/posts/1')
response = con.getresponse()

print("status code:",response.status)
print("Reason:",response.reason)
print("response data:",response.read().decode())