import praw
import csv

# print("Dude")


reddit = praw.Reddit("zhou-rscrape",
         user_agent="zhou-rscrape"
)

url = 'https://old.reddit.com/r/taskmaster/comments/x7g3le/last_tmnz_episode_today_who_do_you_guys_think/'

submission = reddit.submission(url=url)
submission.comments.replace_more(limit=None)
for comment in submission.comments.list():
    print(comment.body)

