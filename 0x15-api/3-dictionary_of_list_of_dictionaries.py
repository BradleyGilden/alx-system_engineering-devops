#!/usr/bin/python3

"""
Records all tasks for all employees
Format must be:
{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"}, ...]}
File name must be: USER_ID.json

Author: Bradley Dillion Gilden
Date: 23-10-2023
"""

import json
import requests


if __name__ == '__main__':
    try:
        statuses = []
        titles = []

        # get all employee tasks
        response = requests.get('https://jsonplaceholder.typicode.com/todos')

        todo_list = response.json()

        for task in todo_list:
            statuses.append(task['completed'])
            titles.append(task['title'])

        # we now need to query user resource to get the usernames
        response = requests.get('https://jsonplaceholder.typicode.com/users')
        users = response.json()
        userlen = len(users)
        # repeats the username and id in a list

        # list comprehension containing dicts all inside a dict comprehension
        json_obj = {str(uid): [{'task': title, 'completed': status,
                                'username': users[uid - 1]['username']}
                               for title, status in zip(titles, statuses)]
                    for uid in range(1, userlen + 1)}

        with open('todo_all_employees.json', 'w') as file:
            json.dump(json_obj, file)

    except Exception:
        pass
