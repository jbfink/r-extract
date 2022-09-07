import praw
import csv
import pandas as pd
import datetime as dt

# print("Dude")


reddit = praw.Reddit("zhou-rscrape",
         user_agent="zhou-rscrape"
)

#url = 'https://old.reddit.com/r/taskmaster/comments/x7g3le/last_tmnz_episode_today_who_do_you_guys_think/'
url = 'https://www.reddit.com/r/antiwork/comments/pdeevi/chinese_millennials_are_choosing_slower_lives_and/'

submission = reddit.submission(url=url)
comments = submission.comments
df_rows = [[comment.author, comment.id, comment.score, comment.body, comment.replies] for comment in comments]
df = pd.DataFrame(df_rows, columns=['Author', 'Comment ID', 'Score', 'Body', "Replies"])
df.to_csv('small.csv')

#submission.comments.replace_more(limit=None)
#for comment in submission.comments.list():
#    print(comment.body)

