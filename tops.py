import praw
import feedparser
import config

reddit = praw.Reddit(user_agent = 'Top Comment Extraction (by /u/caturian)',
                     client_id = config.CLIENT_ID, client_secret = config.CLIENT_SECRET,
                     username = config.USERNAME, password = config.PASSWORD)

length = feedparser.parse(input('Enter an RSS feed:'))
l = len(length)

while l != 0:
    link = length['entries'][l+1]['link']
    submission = reddit.submission(url=link)
    for top_level_comment in submission.comments:
        with open("tops.txt", "a") as tops:
            tops.write(top_level_comment.body)
    l = l - 1
