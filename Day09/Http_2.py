import http.client
import json

con=http.client.HTTPSConnection("jsonplaceholder.typicode.com")

headers = {
    'Content-Type': 'application/json' # what type format we giving
}

payload = json.dumps({
    "title":"Hello World",
    "body":"THis is my body",
    "userId":1
})

con.request('POST', '/posts', headers=headers)

response = con.getresponse()

print("Status code: ", response.status)
print("Reason: ", response.reason)
print("Response: ", response.read().decode())

con.close() #close the connection