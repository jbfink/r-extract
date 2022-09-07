import praw
import csv
import pandas as pd
import datetime as dt

# print("Dude")


reddit = praw.Reddit("zhou-rscrape",
         user_agent="zhou-rscrape"
)

url = 'https://old.reddit.com/r/taskmaster/comments/x7g3le/last_tmnz_episode_today_who_do_you_guys_think/'

submission = reddit.submission(url=url)
comments = submission.comments
df_rows = [[comment.author, comment.parent, comment.id, comment.score, comment.created, comment.body] for comment in comments]
df = pd.DataFrame(df_rows, columns=['Author','Parent ID', 'Comment ID', 'Score', 'Created', 'Body'])
df.to_csv('small.csv')

#submission.comments.replace_more(limit=None)
#for comment in submission.comments.list():
#    print(comment.body)

