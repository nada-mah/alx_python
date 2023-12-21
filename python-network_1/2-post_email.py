import requests 
from sys import argv

if len(argv)> 1:
    URL = argv[1]
    email = argv[2]
    
res = requests.post(URL, data=email)
print(res.text)