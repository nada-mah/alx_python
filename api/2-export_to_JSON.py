"""This module makes 2 api requests and 
uses the informatiom given to write it to a json file
"""

import json
import requests 
from sys import argv

id = argv[1]
url1 = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
empurl= f'https://jsonplaceholder.typicode.com/users/{id}'
# get todo tasks
res1 = requests.get(url1)
data1 = res1.json()
# get employee information
res2 = requests.get(empurl)
employeedata = res2.json()

"""Requred data"""
USER_ID = employeedata['id']
USERNAME = employeedata['username']
TASK_COMPLETED_STATUS = ''
TOTAL_NUMBER_OF_TASKS = len(data1)
TASK_TITLE = ''
tasks = []
for i in range(len(data1)):
    """loop to add task status and title"""
    TASK_COMPLETED_STATUS = data1[i]['completed']
    TASK_TITLE = data1[i]['title']
    tasks.append({"task": TASK_TITLE, "completed": TASK_COMPLETED_STATUS, "username":USERNAME})
    
dictionary={"USER_ID": tasks}
with open(f'{USER_ID}.json', 'w', newline='') as file:
    # write dictionary to json file
    json.dump(dictionary , file)
