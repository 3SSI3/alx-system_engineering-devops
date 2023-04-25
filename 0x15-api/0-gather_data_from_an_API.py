#!/usr/bin/python3
"""Returns info about employee TODO list progress"""
import requests
import sys

employee_id = sys.argv[1]

if __name__ = "__main__":
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    todos = response.json()

    total_tasks = len(todos)
    done = sum(todo["DONE"] for todo in todos)
    progress = done /total_tasks * 100

    employee_name = todos[0]["name"]
    print(f"Employee {employee_name} is done with {done}/{total_tasks} tasks:")
    for todo in todos:
        if todo["DONE"]:
            print("\t{todo['title']}")

