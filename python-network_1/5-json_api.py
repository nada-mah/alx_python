import requests 
import sys 

if len(sys.argv)> 1:
    q = sys.argv[1]
else:
    q=""
URL = 'http://0.0.0.0:5000/search_user'

res = requests.post(URL, data={'q': q })
x=res.json()
print("[{}] {}".format(x["id"], x["name"]))