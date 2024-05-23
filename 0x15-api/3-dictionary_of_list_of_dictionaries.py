#!/usr/bin/python3
"""
a Python script that, using a REST API, for all given
employee ID, returns information about all employees
TODO list progress and exports the data in the json format.
"""

import json
import requests


def TODO_list():

    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(f"{url}users")

    if user_response.status_code != 200:
        print("Unable to fetch user")
        return

    user_data = user_response.json()

    data = {}
    for user in user_data:
        user_id = user["id"]
        todo_response = requests.get(f"{url}users/{user_id}/todos")
        todo_data = todo_response.json()
        user_name = user["username"]
        data[user_id] = []

        for task in todo_data:
            task_list = {
                'username': user_name,
                'task': task["title"],
                'completed': task["completed"],
                }
            data[user_id].append(task_list)

    filename = "todo_all_employees.json"
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(data, file)
    print(f"Data have been exported into {filename}")


if __name__ == "__main__":
    TODO_list()
