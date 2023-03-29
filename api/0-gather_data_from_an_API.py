#!/usr/bin/python3
"""comments"""

import requests
import sys

if __name__ == '__main__':

    try:
        employee_id = int(sys.argv[1])
    except Exception:
        print("parameter is not a integer")
        exit()

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    url = "https://jsonplaceholder.typicode.com/todos/?userId={}".format(
        employee_id)

    done_task = 0
    total_tasks = 0

    response = requests.get(url).json()
    usr_response = requests.get(user_url).json().get('name')

    for task in response:
        total_tasks += 1
        if task['completed'] is True:
            done_task += 1
    print("Employee {} is done with({}/{}):".format(
        usr_response, done_task, total_tasks))

    for task in response:
        if task['completed'] is True:
            print("\t {}".format(task['title']))
