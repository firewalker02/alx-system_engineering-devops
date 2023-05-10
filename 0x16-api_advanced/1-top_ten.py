#!/usr/bin/python3
"""
This is a function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a  subreddit.
"""


import requests

def top_ten(subreddit):
    """
    This is a function that queries the Reddit API
    If the subreddit is non-existent , print None.
    """
   
    request = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        header={"User-Agent": "Custom"},
        parameters={"limit": 10},
    )

# code 200 is the code for OK status
    if request.status_code == 200:
        for get_requestData in request.json().get("data").get("children"):
            newData = get_requestData.get("data")
            redditTitle = newData.get("title")
            print(redditTitle)
    
    # else None is printed
    else:
        print(None)