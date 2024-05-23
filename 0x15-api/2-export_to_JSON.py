#!/usr/bin/python3
"""
a Python script that, using a REST API, for a given
employee ID, returns information about his/her
TODO list progress and  exports the data in the CSV format.
"""

import json
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
    task_list = [{
        'task': task["title"],
        'completed': task["completed"],
        'username': user_data["username"]
         } for task in todo_data]
    all_data = {str(employee_id): task_list}

    filename = f"{employee_id}.json"
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(all_data, file)
    print(f"Data have been exported into {filename}")


if __name__ == "__main__":
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer as the employee ID.")
        sys.exit(1)

    if len(sys.argv) != 2:
        print(f"Usage: python3 script.py {employee_id}")

    TODO_list(employee_id)
