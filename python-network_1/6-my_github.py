import requests 
import sys 

if len(sys.argv)> 1:
    username = sys.argv[1]
    password = sys.argv[2]

URL='https://api.github.com/user'
# res = requests.get(URL, auth=(username,password))
try:
    res = requests.get(URL, auth=(username,password))
    res_json= res.json()
    print(res_json['id'])
except Exception as e:
    print('None')