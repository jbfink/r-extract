import praw
import csv

# print("Dude")


reddit = praw.Reddit("zhou-rscrape",
         user_agent="zhou-rscrape"
)

subreddit = reddit.subreddit("taskmaster")
print(subreddit.title)

filename = 'url-list.csv'
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        print(row)
