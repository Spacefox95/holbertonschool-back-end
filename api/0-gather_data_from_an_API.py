#!/usr/bin/python3
"""
This script displays, based on an id  :
    _ The name (employee_name)
    _ The number of done tasks (number_of_done_tasks)
    _ total_tasks (total_tasks)
    _ Task_title (task_title)
"""

import requests
from sys import argv


def Print_Employee_TODO_LIST(employee_id):
    """ Return API data """
    employee_name_request = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    EMPLOYEE_NAME = employee_name_request.json()['name']
    response_API = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    todolist = response_API.json()
    USER_ID = employee_id
    TOTAL_NUMBER_OF_TASKS = len(todolist)
    task_completed = [task for task in todolist if task['completed']]
    NUMBER_OF_DONE_TASKS = len(task_completed)
    print(
        "Employee {} is done with tasks({}/{}):".format(
            EMPLOYEE_NAME,
            NUMBER_OF_DONE_TASKS,
            TOTAL_NUMBER_OF_TASKS))
    for task in task_completed:
        TASK_TITLE = task['title']
        print("\t {}".format(TASK_TITLE))


if __name__ == "__main__":
    employee_id = int(argv[1])
    Print_Employee_TODO_LIST(employee_id)
