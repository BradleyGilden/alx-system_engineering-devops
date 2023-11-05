#!/usr/bin/python3

"""
queries the Reddit API and prints the titles of the first 10 hot posts listed
for a given subreddit.

Author: Bradley Dillion Gilden
Date: 05-11-2023
"""
import requests


def top_ten(subreddit):
    """counts number of subscribers of a specific subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "ComaScript/1.77"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
    else:
        data = response.json()
        if (data.get('data') is None or
           data['data'].get('children') is None):
            print(None)
        else:
            posts = data['data']['children']
            if len(posts) < 2:
                print(None)
            else:
                for i in range(0, 10):
                    print(posts[i]['data']['title'])
