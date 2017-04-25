# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from textblob import TextBlob
import praw

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

#Obtaining /r/wholesomememes as my target subreddit instance and a quick check to make sure
    # that everything works
subreddit = redditinstance.subreddit('wholesomememes')
print(subreddit.display_name)
print(subreddit.title)

#This is leftover from using the live connection with reddit
commentslist = []
for comment in redditinstance.subreddit('wholesomememes').comments(limit=60):
    commentslist.append(comment.body)

#Using textblob to do semantic analysis on each comment, finding the comments
    # that are more subjective than objective, and adding them to a list which
    # we then calculate the average of to compare against other subreddits.

Subredditlist = []
#Automate searching through my prepopulated list of subreddits
def sentianalyze(Subreddit):
    bloblist = []
    sentiset = []
    for x in commentslist:
        bloblist.append(TextBlob(x))    
        for comment in bloblist:
            if comment.sentiment.subjectivity > 0:
                sentiset.append(comment.sentiment.polarity)        
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1) 
print mean(sentiset)  


  

