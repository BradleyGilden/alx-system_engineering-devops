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


if __name__ == "__main__":
    try:
        url = "https://jsonplaceholder.typicode.com/todos?userId={}"

        response = requests.get("https://jsonplaceholder.typicode.com/users")
        users = response.json()

        # dict comprehends users while list comprehending responses
        json_obj = {
            str(u["id"]): [
                {
                    "username": u["username"],
                    "task": task["title"],
                    "completed": task["completed"],
                }
                for task in requests.get(url.format(u["id"])).json()
            ]
            for u in users
        }

        with open("todo_all_employees.json", "w") as file:
            json.dump(json_obj, file)

    except Exception:
        pass
