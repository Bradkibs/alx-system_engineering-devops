#!/usr/bin/python3

"""
A script to return information about
Todos list progress of employees given
their ID's
"""

import requests
import sys


url_1 = 'https://jsonplaceholder.typicode.com/todos'
url_2 = 'https://jsonplaceholder.typicode.com/users'
payload = {'userId': str(sys.argv[1])}
try:
    req_1 = requests.get(url_2)
    json_1 = req_1.json()
    idx = int(sys.argv[1])
    count = 0
    completed = 0
    titles = []
    for i in json_1:
        if i.get("id") == idx:
            name = i.get("name")
    req_2 = requests.get(url_1, params=payload)
    json_2 = req_2.json()
    for j in json_2:
        count += 1
        if j.get("completed"):
            completed += 1
            titles.append(j.get("title"))
    print(f"Employee {name} is done with tasks({completed}/{count}):")
    [print("\t" + " " + t) for t in titles]
except Exception as e:
    print("Error! " + str(e))
