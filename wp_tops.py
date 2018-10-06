import praw
import feedparser

reddit = praw.Reddit(user_agent='Comment Extraction (by /u/jetcoff)',
                     client_id='PFyJAFK1hMVFlg', client_secret="wIQgqph3fB2Lo_b1X4zs9t4PYO0",
                     username='caturian', password='Brolingo101')

length = feedparser.parse(input('Enter an RSS feed:'))
l = len(length)

while l != 0:
    link = length['entries'][l+1]['link']
    submission = reddit.submission(url=link)
    for top_level_comment in submission.comments:
        with open("tops.txt", "a") as tops:
            tops.write(top_level_comment.body)
    l = l - 1
