#!/usr/bin/python3
"""
Getting data from a rest API and exporting it to a
CSV file
"""
import requests
import sys


""" A simple Csv writing script """


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please enter the user Id you wish to find details about")
        sys.exit()
    url = "https://jsonplaceholder.typicode.com"
    payload = {'userId' : int(sys.argv[1])}
    try:
        users_req = requests.get("{}/users?id={}".format(url, int(sys.argv[1])), params=payload).json()
        todos_req = requests.get("{}/todos".format(url), params=payload).json()
        name = users_req[0]["username"]
        completed_status = [todos_req[i]["completed"] for i in range(len(todos_req))]
        file_out = str(sys.argv[1]) + ".csv"
        count = 0
        with open(file_out, 'w') as csvfile:
            for todo in todos_req:
                csvfile.write('"{}","{}","{}","{}"\n'.format(sys.argv[1],
                                                             name,
                                                             completed_status[count],
                                                             todo.get("title")
                                                             )
                             )
                count += 1
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(f"Error! {exc_type} occured at line {exc_tb.tb_lineno}")
