#!/usr/bin/python3
"""a function that queries the Reddit API to print the
title of the first 10 hot posts listed for a given
subreddit
"""


import json
import requests


def top_ten(subreddit):
    """
    returns a valid list of 10 hot titles of the subreddit
    passed as argument. If not a valid subreddit will print
    None
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    header = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=header, allow_redirects=False)

    if resp.status_code == 200:
        children = resp.json().get("data").get("children")
        titles = [child.get("data").get("title") for child in children]
        output = "\n".join(titles)
        print(output)
    else:
        print(None)
