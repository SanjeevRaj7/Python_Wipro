#login

import requests
base_url="https://reqres.in/"

def login_and_gettoken(email,password):
    loginurl = f"{base_url}/api/login"

    payload = {
        "email":email,
        "password":password,
    }

    response = requests.post(loginurl,json=payload)

    if response.status_code == 200:
        print("Login Successful")
        token = response.json().get("token")
        print("token:",token)
        return token
    else:
        print("Login failed with status code:", response.status_code)
        print("Response:",response.json())
        return None

def fetch_protected_data(token):
    protectedurl = f"{base_url}/api/users?page=2"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(protectedurl,headers=headers)
    if response.status_code == 200:
        print("Protected Data Fetched")
        print("data:",response.json())
    else:
        print("unable to fetch protected data status code:", response.status_code)
        print("response:",response.json())



if __name__ == "__main__":
    email= "eve.holt@reqres.in"
    password = "pistol"
    token = login_and_gettoken(email,password)
    print(token)

    if token:
        fetch_protected_data(token)
