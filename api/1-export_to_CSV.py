import csv
import requests 
from sys import argv

from sqlalchemy import null

def get_task(id):
    url1 = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
    empurl= f'https://jsonplaceholder.typicode.com/users/{id}'

    res1 = requests.get(url1)
    data1 = res1.json()

    res2 = requests.get(empurl)
    employeedata = res2.json()

    USER_ID = str(employeedata['id']) 
    USERNAME = employeedata['username']
    TASK_COMPLETED_STATUS = ''
    TOTAL_NUMBER_OF_TASKS = len(data1)
    TASK_TITLE = ''

    with open(f'api/{id}.csv', 'w') as file:
        writer = csv.writer(file,quotechar="'")
        for i in range(len(data1)):
            TASK_COMPLETED_STATUS = data1[i]['completed']
            TASK_TITLE = data1[i]['title']
            writer.writerow([ '"'+USER_ID+'"', '"'+USERNAME+'"', '"'+str(TASK_COMPLETED_STATUS)+'"', '"'+TASK_TITLE+'"' ])
if __name__ == "__main__":
    for id in range(1,11):
        get_task(str(id))