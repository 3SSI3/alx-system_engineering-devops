#!/usr/bin/python3

"""
 Titles of the first 10 hot post listed for given subreddit
"""
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 404:
        data = response.json()['data']['children']
        for post in data:
            print(post['data']['title'])
    else:
        print(None)
