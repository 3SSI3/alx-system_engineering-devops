#!/usr/bin/python3

"
 Titles of the first 10 hot post listed for given subsreddit
"
import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()['data']['children']
        for post in data:
            print(post['data']['title'])
    else:
        print(None)
