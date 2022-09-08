import praw
import csv
import pandas as pd
import datetime as dt



reddit = praw.Reddit("zhou-rscrape",
         user_agent="zhou-rscrape"
)

urls = 'url-list.csv'

with open(urls, 'r') as csvfile:
    datareader = list(csv.reader(csvfile, delimiter = ","))
    number = 1
    for row in datareader:
        submission = reddit.submission(url=row[number])
        submission.comments.replace_more(limit=None)
        comments = submission.comments.list()
        df_rows = [[comment.author, comment.id, comment.score, comment.body] for comment in comments]
        df = pd.DataFrame(df_rows, columns=['Author', 'Comment ID', 'Score', 'Body', ])
        df.to_csv(f'file{number}.csv')
        number = number + 1
        print(number)

 

#url = 'https://www.reddit.com/r/antiwork/comments/pdeevi/chinese_millennials_are_choosing_slower_lives_and/'

#submission = reddit.submission(url=url)
#comments = submission.comments.list()
#df_rows = [[comment.author, comment.id, comment.score, comment.body] for comment in comments]
#df = pd.DataFrame(df_rows, columns=['Author', 'Comment ID', 'Score', 'Body', ])
#df.to_csv('small.csv')


