#!/usr/bin/python3
"""
This script export data in Json format :
    _ The user_id (employee_id)
    _ The username (username)
    _ Task_completed_stats (new_task_status)
    _ Task_title (new_task_title)
"""

from sys import argv
import json
import requests


def Print_Employee_TODO_LIST(employee_id):
    """ Return API data """
    employee_name_request = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    USERNAME = employee_name_request.json()['username']
    USER_ID = employee_id
    response_API = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    todolist = response_API.json()
    with open("{}.json".format(employee_id), 'w') as file:
        tasks_list = []
        for new_task in todolist:
            TASK_TITLE = new_task['title']
            TASK_COMPLETED_STATUS = new_task['completed']
            task_data = {
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME
                }
            tasks_list.append(task_data)
        json.dump({str(USER_ID): tasks_list}, file)


if __name__ == "__main__":
    employee_id = int(argv[1])
    Print_Employee_TODO_LIST(employee_id)
