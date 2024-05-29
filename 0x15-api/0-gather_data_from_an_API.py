#!/usr/bin/python3
"""Returns todo list information for a given employee ID."""
import requests
import sys
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = request.get(url + "users/{}".format(sys.argv[1])).json()
    todos = request.get(url + "todos", params={"userId": sys.argv[1]}).json()
    finished = [t.get('title') fo t in todos if t.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(finished), len(todos)))
    [print("\t {}".format(c)) for c in finished]
