#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers for a given subreddit.
"""


import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers on a subreddit """
        
        
    header = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code != 200:
        return 0
    data = response.json()
    return data['data']['subscribers']
