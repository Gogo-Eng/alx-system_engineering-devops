#!/usr/bin/python3
"""
a Python script that, using a REST API, for a given
employee ID, returns information about his/her T
ODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    if len(sys.argv) != 2:
        print(f"Usage: python3 script.py {employee_id}")

    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(f"{url}users/{employee_id}")

    if user_response.status_code != 200:
        print("Unable to fetch user")

    user_data = user_response.json()
    employee_name = user_data.get('name')
    if not employee_name:
        print("Employee name not found")

    todo_response = requests.get(f"{url}todos?userId={employee_id}")

    if todo_response.status_code != 200:
        print("Unable to fetch TODO data")

    todo_data = todo_response.json()
    completed_tasks = []
    for task in todo_data:
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))

    nct = len(completed_tasks)
    tnt = len(todo_data)

    print(f"Employee {employee_name} is done with tasks({nct}/{tnt}):")
    for tasks in completed_tasks:
        print(f"\t {tasks}")
