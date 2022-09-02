import praw

# print("Dude")


reddit = praw.Reddit("zhou-rscrape",
         user_agent="zhou-rscrape"
)

subreddit = reddit.subreddit("taskmaster")
print(subreddit.title)

