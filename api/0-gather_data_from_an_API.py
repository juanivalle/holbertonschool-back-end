#!/usr/bin/python3
"""comments"""

import requests
import sys

if __name__ == '__main__':

    USER_ID = sys.argv[1]
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    done_tasks = requests.get(todos_url, params={
        'completed': 'True', 'user_Id': USER_ID}).json
    total_task = requests.get(todos_url, params={'userId': USER_ID}).json()
    info = requests.get(users_url, params={'id': USER_ID}).json()

    EMPLOYEE_NAME = info[0]['name']
    num_done_tasks = len(done_tasks)
    num_total_tasks = len(total_task)

    print('Employee {} is done with tasks({}/{}):'.format(
        EMPLOYEE_NAME, num_done_tasks, num_total_tasks))

    for task in done_tasks:
        print("\t {}".format(task['title']))
