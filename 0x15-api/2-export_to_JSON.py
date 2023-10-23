#!/usr/bin/python3

"""
Records all tasks that are owned by this employee
Format must be:
{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"}, ...]}
File name must be: USER_ID.json

Author: Bradley Dillion Gilden
Date: 23-10-2023
"""

import requests
from sys import argv
import json


if __name__ == '__main__':
    try:
        tasks_status = []
        tasks_tot = 0
        titles = []
        id = argv[1]

        # user id from argument to be used to get all todo's for that user
        params = {'userId': id}
        # get employee tasks assigned and completed as well as their id
        response = requests.get(
            'https://jsonplaceholder.typicode.com/todos', params=params)

        todo_list = response.json()

        for task in todo_list:
            tasks_status.append(task['completed'])
            titles.append(task['title'])
            tasks_tot += 1

        # we now need to query user resource to get the username
        response = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{id}')
        username = response.json()['username']
        # repeats the username and id in a list

        # list comprehension for dict representation of all tasks
        json_list = [{'task': title, 'completed': status,
                      'username': username}
                     for title, status in zip(titles, tasks_status)]

        json_obj = {str(id): json_list}

        with open(f'{id}.json', 'w') as file:
            json.dump(json_obj, file)

    except Exception:
        pass
