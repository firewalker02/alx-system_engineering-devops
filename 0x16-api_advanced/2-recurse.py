#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function returns None.
"""

import requests


def recurse(subreddit, hot_List=[], afterReddit=""):
    
    
    """
    This is a function that queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit.

     If the subreddit is non-existent, return None.
    """
    # the API is queried
    request = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        
        headers= {"User-Agent": "Custom"},
        
        parameters= {"after": afterReddit},
    )

   # code 200 is the code for OK status
    if request.status_code == 200:
        
        # Gets the appriopriate hot titles of the list using recursion
        for get_redditData in request.json().get("data").get("children"):
            newData = get_redditData.get("data")
            title = newData.get("title")
            hot_List.append(title)
        
        afterReddit = request.json().get("data").get("after")

        if afterReddit is None:
            return hot_List
        else:
            return recurse(subreddit, hot_List, afterReddit)
    # else None is returned
    
    else:
        
      return None