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
    datareader = list(csv.reader(csvfile, delimiter=","))
    print(datareader)
    datareader = datareader[0]
    print(type(datareader))
    #number = 1
    for item in datareader:
        print(item)
        #number = number + 1

