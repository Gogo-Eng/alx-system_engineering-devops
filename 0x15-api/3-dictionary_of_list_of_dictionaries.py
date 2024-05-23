#!/usr/bin/python3
''' Using what you did in the task #0, extend your Python script to export data
in the JSON format.'''

from json import dump
from requests import get


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = get(url)
    users = response.json()

    dictionary = {}
    for user in users:
        user_id = user['id']
        username = user['username']
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        response = get(url)
        tasks = response.json()
        dictionary[user_id] = []
        for task in tasks:
            task_list = {
                "username": username,
                "task": task['title'],
                "completed": task['completed'],
                }
            dictionary[user_id].append(task_list)

    with open('todo_all_employees.json', 'w') as file:
        dump(dictionary, file)
