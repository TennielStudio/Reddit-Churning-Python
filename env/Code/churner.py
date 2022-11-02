import praw
import pandas as pd

reddit_read_only = praw.Reddit(client_id="",         # your client id
                               client_secret="",      # your client secret
                               user_agent="")        # your user agent

subreddit = reddit_read_only.subreddit("churning")

# print("Display Name: ", subreddit.display_name)

# print("Title: ", subreddit.title)

# print("Description: ", subreddit.description)

posts = subreddit.top("year")

posts_dict = {"Title": [], "Post Text": [], "ID": [], "Score": [],
              "Total Comments": [], "Post URL": []}

for post in posts:
    posts_dict["Title"].append(post.title)

    posts_dict["Post Text"].append(post.selftext)

    posts_dict["ID"].append(post.id)

    posts_dict["Score"].append(post.score)

    posts_dict["Total Comments"].append(post.num_comments)

    posts_dict["Post URL"].append(post.url)

top_yearly_posts = pd.DataFrame(posts_dict) # create a pandas data frame to store the top yearly posts
print(top_yearly_posts)

