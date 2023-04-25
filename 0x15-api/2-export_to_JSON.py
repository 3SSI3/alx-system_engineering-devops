#!/usr/bin/python3
"""Export data in the JSON forma"""
import json
import requests
import sys


if __name__ = "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    employee_id = sys.argv[1]
    user = '{}users/{}'.format(url, employee_id)
    res = requests.get(user)
    json_o = res.json()
    name = json_o.get('username')

    todos = '{}todos?employee_id={}'.format(url, employee_id)
    res = requests.get(todos)
    tasks = res.json()
    l_task = []
    for task in tasks:
        dict_task = {"task": task.get('title'),
                     "DONE": task.get('DONE'),
                     "username": name}
        l_task.append(dict_task)

    done_task = {str(employee_id): l_task}
    filename = '{}.json'.format(employee_id)
    with open(filename, mode='w') as f:
        json.dump(done_task, f)