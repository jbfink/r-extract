import praw
import csv
import pandas as pd
import datetime as dt



reddit = praw.Reddit("zhou-rscrape",
         user_agent="zhou-rscrape"
)

urls = 'url-list.csv'

with open(urls, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        number = 1
        submission = reddit.submission(url=row[number])
        submission.comments.replace_more(limit=None)
        comments = submission.comments.list()
        df_rows = [[comment.author, comment.id, comment.score, comment.body] for comment in comments]
        df = pd.DataFrame(df_rows, columns=['Author', 'Comment ID', 'Score', 'Body', ])
        df.to_csv('notgonnawork.csv')
        number = number + 1

 

#url = 'https://www.reddit.com/r/antiwork/comments/pdeevi/chinese_millennials_are_choosing_slower_lives_and/'

#submission = reddit.submission(url=url)
#comments = submission.comments.list()
#df_rows = [[comment.author, comment.id, comment.score, comment.body] for comment in comments]
#df = pd.DataFrame(df_rows, columns=['Author', 'Comment ID', 'Score', 'Body', ])
#df.to_csv('small.csv')


