#!/usr/bin/python3
"""
This script displays, based on an id  :
    _ The name (employee_name)
    _ The number of done tasks (number_of_done_tasks)
    _ total_tasks (total_tasks)
    _ Task_title (task_title)
"""

import json
import requests
from sys import argv


def Print_Employee_TODO_LIST(employee_id):
    employee_name_request = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee_name = employee_name_request.json()['name']
    response_API = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    todolist = response_API.json()
    total_tasks = len(todolist)
    task_completed = [task for task in todolist if task['completed']]
    number_of_done_tasks = len(task_completed)
    print(
        f"Employee {employee_name} is done\
              with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in task_completed:
        task_title = task['title']
        print("\t {}".format(task_title))


if __name__ == "__main__":
    employee_id = int(argv[1])
    Print_Employee_TODO_LIST(employee_id)
