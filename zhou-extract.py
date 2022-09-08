import praw
import csv
import pandas as pd
import datetime as dt

# print("Dude")


reddit = praw.Reddit("zhou-rscrape",
         user_agent="zhou-rscrape"
)

url = 'https://www.reddit.com/r/antiwork/comments/pdeevi/chinese_millennials_are_choosing_slower_lives_and/'

submission = reddit.submission(url=url)
comments = submission.comments.list()
df_rows = [[comment.author, comment.id, comment.score, comment.body] for comment in comments]
df = pd.DataFrame(df_rows, columns=['Author', 'Comment ID', 'Score', 'Body', ])
df.to_csv('small.csv')


