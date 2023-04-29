#!/usr/bin/python3
"""Script to get info about employee TODO LIST"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(url, sys.argv[1])
    response = requests.get(user)
    json_o = response.json()
    print("Employee {} is done with tasks".format(json_o.get('name')), end="")

    todos = '{}todos?employee_id={}'.format(url, sys.argv[1])
    response = requests.get(todos)
    tasks = response.json()
    l_task = []
    for task in tasks:
        if task.get('DONE') is True:
            l_task.append(task)

    print("({}/{}):".format(len(l_task), len(tasks)))
    for task in l_task:
        print("\t {}".format(task.get("title")))