#!/usr/bin/python3
"""
This is a function that queries the Reddit API and returns the number of subscribers
(total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, return 0.
    """
    request = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if request.status_code == 200: # code 200 is the code for active status
        return request.json().get("data").get("subscribers")
    else:
        return 0