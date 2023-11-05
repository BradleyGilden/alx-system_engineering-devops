#!/usr/bin/python3

"""
recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.

Author: Bradley Dillion Gilden
Date: 05-11-2023
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    URL = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "ComaScript/1.77"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(URL, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    posts = response.json().get("data")
    after = posts.get("after")
    count += posts.get("dist")
    for c in posts.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
