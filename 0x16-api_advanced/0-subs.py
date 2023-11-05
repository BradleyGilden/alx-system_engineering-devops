#!/usr/bin/python3

"""
counts number of subscribers of a specific subreddit

Author: Bradley Dillion Gilden
Date: 05-11-2023
"""
import requests


def number_of_subscribers(subreddit):
    """counts number of subscribers of a specific subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "ComaScript/1.77"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    else:
        data = response.json()
        if (data.get('data') is None or
           data['data'].get('subscribers') is None):
            return 0
        return int(data['data']['subscribers'])
