# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from textblob import TextBlob
import praw
import numpy as np

#Access Reddit API and authenticate bot through OAuth2 
redditinstance = praw.Reddit(client_id='EBLOq3xVjVAuBA',
                     client_secret='m4Ny_xg9YFIAUB-1R-nNKp_JcXQ',
                     user_agent='test script for /u/WholesomenessBot',
                     username='WholesomenessBot',
                     password='605557')
#Just checking to make sure I'm the right user, and that I'm not read-only; 
    # read_only should be false
print(redditinstance.read_only)
print(redditinstance.user.me())

#Put the subreddit and keyword that you want to search for here
SUBREDDIT = "pcmasterrace"
KEYWORD = "nvidia"

#Obtaining target subreddit instance and a quick check to make sure that everything works
subreddit = redditinstance.subreddit(SUBREDDIT)
print "You are currently querying the subreddit:", subreddit.display_name, ", please wait..."
print(subreddit.title)

#Getting all comments in SUBREDDIT that mention KEYWORD to analyze
commentslist = []
for comment in redditinstance.subreddit(SUBREDDIT).comments(limit=5000):
    if KEYWORD in comment.body:
        commentslist.append(comment.body)
        
blobbin = []
for s in commentslist:
    blobbin.append(TextBlob(s))

#Sentiment analysis info
sentiment = []    
for x in blobbin:
    sentiment.append(x.sentiment.polarity)
print "The average sentiment polarity of", KEYWORD, "is", np.average(sentiment), "pulled from", len(commentslist), "comments."
    
#Be careful with requests, too many comment requests and you'll get a 429 error code.

