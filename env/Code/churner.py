import praw
import pandas as pd

reddit_read_only = praw.Reddit(client_id="",         # your client id
                               client_secret="",      # your client secret
                               user_agent="")        # your user agent

subreddit = reddit_read_only.subreddit("churning")

print("Display Name: ", subreddit.display_name)

print("Title: ", subreddit.title)

print("Description: ", subreddit.description)
 