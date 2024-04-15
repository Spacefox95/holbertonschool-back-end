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


def Print_Employee_TODO_LIST():
    employee_name_request = requests.get(
        f'https://jsonplaceholder.typicode.com/users')
    user_data = employee_name_request.json()
    username = {}
    for user in user_data:
        username[user['id']] = user['username']
    response_API = requests.get(
        f'https://jsonplaceholder.typicode.com/todos')
    todolist = response_API.json()
    with open("todo_all_employees.json", 'w') as file:
        tasks_by_user = {}
        for new_task in todolist:
            user_id = new_task['userId']
            if user_id not in tasks_by_user:
                tasks_by_user[user_id] = []
            new_task_title = new_task['title']
            new_task_status = new_task['completed']
            user_id = new_task['userId']
            task_data = {
                "username": username[user_id],
                "task": new_task_title,
                "completed": new_task_status
                }
            tasks_by_user[user_id].append(task_data)
        json.dump(tasks_by_user, file)


if __name__ == "__main__":
    Print_Employee_TODO_LIST()
