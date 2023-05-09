#!/usr/bin/python3
"""
   Queries the Reddit API and returns the num of subscribers (not active users, total subscribers) for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by/u/bdov_)'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0
