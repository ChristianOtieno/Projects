
import sys

import matplotlib.pyplot as plt
import tweepy
from textblob import TextBlob


def percentage (part, whole):
    return 100 * float(part)/float(whole)

consumerKey = "XXXXXXXXXXXXXXXXXXXXXXX"
consumerSecret = "XXXXXXXXXXXXXXXXXXXXXXXXX"
accessToken = "XXXXXXXXXXXXXXXXXXXXXXXX"
accessTokenSecret = "XXXXXXXXXXXXXXXXXXXX"

auth = tweepy.OAuthHandler(consumerKey,consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

searchTerm = input("Enter keyword/hashtag to search about: ")
noOfSearchTerms = int(input("Enter how many tweets to analyze: "))

tweets = tweepy.Cursor(api.search, q=searchTerm, lang="English").items(noOfSearchTerms)


positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
