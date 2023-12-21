import requests 
import sys 

if len(sys.argv)> 1:
    URL = sys.argv[1]
    
res = requests.get(URL)
status = res.status_code
if status >=400:
    print('Error code: {}'.format(status))
else:
    print(res.text)