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
    datareader = datareader[0]
    # this is needed because the list returned is a *nested* list, viz, one that is [[ <blah, blah, blah> ]], and just trying to access it directly means you get the *one* element of the original list. Using [0] effectively strips out the extra brackets.
    number = 1
    for row in datareader:
        print(number)
        submission = reddit.submission(url=row)
        submission.comments.replace_more(limit=None)
        comments = submission.comments.list()
        df_rows = [[comment.author, comment.id, comment.score, comment.body] for comment in comments]
        df = pd.DataFrame(df_rows, columns=['Author', 'Comment ID', 'Score', 'Body', ])
        df.to_csv(f'file{number}.csv')
        number = number + 1

 



