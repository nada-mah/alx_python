#!/usr/bin/python3
'''
output employee todo tasks to a json file 
from an api
'''
import json
import requests 
from sys import argv

id = argv[1]
url1 = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
empurl= f'https://jsonplaceholder.typicode.com/users/{id}'

res1 = requests.get(url1)
data1 = res1.json()

res2 = requests.get(empurl)
employeedata = res2.json()

USER_ID = employeedata['id']
USERNAME = employeedata['username']
TASK_COMPLETED_STATUS = ''
TOTAL_NUMBER_OF_TASKS = len(data1)
TASK_TITLE = ''
tasks = []
for i in range(len(data1)):
    TASK_COMPLETED_STATUS = data1[i]['completed']
    TASK_TITLE = data1[i]['title']
    tasks.append({"task": TASK_TITLE, "completed": TASK_COMPLETED_STATUS, "username":USERNAME})
    
dictionary={"USER_ID": tasks}
with open(f'{USER_ID}.json', 'w', newline='') as file:
    json.dump(dictionary , file)
