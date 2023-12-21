import requests 
import sys 

if len(sys.argv)> 1:
    URL = sys.argv[1]
    email = sys.argv[2]
    
res = requests.post(URL, data={'email': email})
print(res.text)