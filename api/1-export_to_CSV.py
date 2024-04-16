#!/usr/bin/python3
"""
This script displays :
    _ The user_id (employee_id)
    _ The username (username)
    _ Task_completed_stats (new_task_status)
    _ Task_title (new_task_title)
"""
import csv
import requests
from sys import argv


def Print_Employee_TODO_LIST(employee_id):
    """ Return API data """
    employee_name_request = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    USERNAME = employee_name_request.json()['username']
    response_API = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    todolist = response_API.json()
    USER_ID = employee_id
    with open("{}.csv".format(USER_ID), 'w') as file:
        formatting = ["USER_ID",
                      "USERNAME",
                      "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        writer = csv.DictWriter(
            file, fieldnames=formatting, quoting=csv.QUOTE_ALL)
        for new_task in todolist:
            TASK_TITLE = new_task['title']
            TASK_COMPLETED_STATUS = new_task['completed']
            writer.writerow({"USER_ID": USER_ID, "USERNAME": USERNAME,
                             "TASK_COMPLETED_STATUS": TASK_COMPLETED_STATUS,
                             "TASK_TITLE": TASK_TITLE})


if __name__ == "__main__":
    employee_id = int(argv[1])
    Print_Employee_TODO_LIST(employee_id)
