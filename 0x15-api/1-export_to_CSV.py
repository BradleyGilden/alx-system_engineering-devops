#!/usr/bin/python3

"""
+ Records all tasks that are owned by this employee
+ Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
+ File name must be: USER_ID.csv

Author: Bradley Dillion Gilden
Date: 23-10-2023
"""

from sys import argv

import requests

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

        with open(f'{id}.csv', 'w') as file:
            for i in range(tasks_tot):
                file.write(
                    f'"{id}","{username}","{tasks_status[i]}","{titles[i]}"\n')
    except Exception:
        pass