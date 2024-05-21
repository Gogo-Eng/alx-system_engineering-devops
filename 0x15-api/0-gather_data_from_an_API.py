#!/usr/bin/python3
"""
a Python script that, using a REST API, for a given
employee ID, returns information about his/her T
ODO list progress.
"""

import requests
import sys


def TODO_list(employee_id):

    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(f"{url}users/{employee_id}")

    if user_response.status_code != 200:
        print("Unable to fetch user")
        return

    user_data = user_response.json()
    employee_name = user_data['name']
    if not employee_name:
        print("Employee name not found")
        return

    todo_response = requests.get(f"{url}todos?userId={employee_id}")

    if todo_response.status_code != 200:
        print("Unable to fetch TODO data")
        return
    todo_data = todo_response.json()
    completed_tasks = []
    for task in todo_data:
        if task["completed"] is True:
            completed_tasks.append(task['title'])

    number_of_completed_tasks = len(completed_tasks)
    total_number_of_tasks = len(todo_data)

    print(f"Employee {employee_name} is done with \
           tasks({number_of_completed_tasks}/{total_number_of_tasks}):")
    for tasks in completed_tasks:
        print(f"\t {tasks}")


if __name__ == "__main__":
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer as the employee ID.")
        sys.exit(1)

    if len(sys.argv) != 2:
        print(f"Usage: python3 script.py {employee_id}")

    TODO_list(employee_id)
