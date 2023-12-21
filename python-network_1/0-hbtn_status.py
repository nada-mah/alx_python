import requests

url ='https://alu-intranet.hbtn.io/status'
res = requests.get(url)

print("Body response:")
print("\t- type: {}".format(type(res.text)))
print("\t- content: {}".format(res.text))