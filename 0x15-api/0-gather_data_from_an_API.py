#!/usr/bin/python3

"""
+ The script must display on the standard output the employee TODO list
progress in this exact format:
+ First line: Employee EMPLOYEE_NAME is done with
tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    - EMPLOYEE_NAME: name of the employee
    - NUMBER_OF_DONE_TASKS: number of completed tasks
    - TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of
    completed and non-completed tasks
+ Second and N next lines display the title of completed tasks:
TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)

Author: Bradley Dillion Gilden
Date: 23-10-2023
"""

import requests
from sys import argv

if __name__ == '__main__':
    try:
        complete = 0
        tasks_tot = 0
        titles = []

        # user id from argument to be used to get all todo's for that user
        params = {'userId': argv[1]}
        # get employee tasks assigned and completed as well as their id
        response = requests.get(
            'https://jsonplaceholder.typicode.com/todos', params=params)

        todo_list = response.json()

        for task in todo_list:
            if task['completed'] is True:
                titles.append(task['title'])
                complete += 1
            tasks_tot += 1

        # we now need to query user resource to get the users name
        response = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
        name = response.json()['name']

        print(
            f'Employee {name} is done with tasks({complete}/{tasks_tot}):')
        for title in titles:
            print(f'\t {title}')

    except Exception:
        pass
