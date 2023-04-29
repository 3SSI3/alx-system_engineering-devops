#!/usr/bin/python3
"""Export data in the JSON forma"""
import json
import requests
import sys

if __name__ == "__main__":
    employer_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(employer_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": employer_id}).json()

    with open("{}.json".format(employer_id), "w") as jsonfile:
        json.dump({employer_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)
