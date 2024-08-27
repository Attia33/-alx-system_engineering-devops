#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Recursively fetches all hot articles for a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'my-custom-user-agent'}
    params = {'after': after}

    try:
        response = requests.get(
    url,
    headers=headers,
    params=params,
     allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            after = data['data']['after']
            if not posts:
                return hot_list
            hot_list.extend([post['data']['title'] for post in posts])
            if after:
                return recurse(subreddit, hot_list, after)
            return hot_list
        else:
            return None
         except requests.RequestException:
             return None
