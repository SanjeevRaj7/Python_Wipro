import http.client
import ssl
context = ssl.create_default_context()
con = http.client.HTTPSConnection("jsonplaceholder.typicode.com",context=context)

con.request("GET","/posts/77")

response = con.getresponse()
print("status codee:",response.status)
print("reason:",response.reason)
print("response:",response.read().decode())