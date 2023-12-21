import requests 
from sys import argv

if len(argv)> 1:
    URL = argv[1]
    res = requests.get(URL)

    print(res.headers['X-Request-Id'])