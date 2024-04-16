#!/usr/bin/python3
"""
This script export data in Json format :
    _ The user_id (employee_id)
    _ The username (username)
    _ Task_completed_stats (new_task_status)
    _ Task_title (new_task_title)
"""
import requests
import json
from sys import argv


def Print_Employee_TODO_LIST(employee_id):
    """ Return API data """
    employee_name_request = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    username = employee_name_request.json()['username']
    response_API = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    todolist = response_API.json()
    with open("{}.json".format(employee_id), 'w') as file:
        tasks_list = []
        for new_task in todolist:
            new_task_title = new_task['title']
            new_task_status = new_task['completed']
            task_data = {
                "task": new_task_title,
                "completed": new_task_status,
                "username": username
                }
            tasks_list.append(task_data)
        json.dump({str(employee_id): tasks_list}, file)


if __name__ == "__main__":
    employee_id = int(argv[1])
    Print_Employee_TODO_LIST(employee_id)
