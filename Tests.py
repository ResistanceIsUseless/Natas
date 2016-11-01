import string

alphanum = string.ascii_letters + string.digits
print (alphanum)
for i in alphanum:
    print(i)
import requests
import json



def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(response.text)
        print(response.status_code)

for i in range(30): # 30 NBA Teams
    base_url = "http://stats.nba.com/stats/teamdetails?teamID="   
    team_url = base_url + str(team_id)
    data = get_data(team_url)