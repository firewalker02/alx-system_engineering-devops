#!/usr/bin/python3
"""
This is a function that queries the Reddit API and returns the number of subscribers
(total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""

import requests


def number_of_subscribers(subreddit):
    """
    This is a function that queries the Reddit API
    If the sub reddit is non existent, returns 0.
    """
    request = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    # code 200 is the code for OK status
    if request.status_code == 200: 
        return request.json().get("data").get("subscribers")
    # else 0 is returned
    else:
        return 0