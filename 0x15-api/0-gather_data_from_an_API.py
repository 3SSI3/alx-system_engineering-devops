#!/usr/bin/python3
"""To do list info of given Employee ID"""
import requests
import sys

EMPLOYEE_API_URL = "https://jsonplaceholder.typicode.com/users/{id}"
TODO_API_URL = "https://jsonplaceholder.typicode.com/todos?userId={id}"


def get_employee_name(employee_id):
    employee_data = requests.get(EMPLOYEE_API_URL.format(id=employee_id)).json()
    return employee_data['name']


def get_todo_list_progress(employee_id):
    todo_data = requests.get(TODO_API_URL.format(id=employee_id)).json()
    total_tasks = len(todo_data)
    done_tasks = sum([1 for task in todo_data if task['completed']])
    return done_tasks, total_tasks, [task['title'] for task in todo_data if task['completed']]


def display_todo_list_progress(employee_id):
    employee_name = get_employee_name(employee_id)
    done_tasks, total_tasks, completed_tasks = get_todo_list_progress(employee_id)
    print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")


# example usage
display_todo_list_progress(1)
