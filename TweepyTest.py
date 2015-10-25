import tweepy
import Passwords as passwords
import json
import random
from tweepy.parsers import JSONParser

auth = tweepy.OAuthHandler(passwords.apiKey, passwords.apiSecret)

auth.set_access_token(passwords.access_token, passwords.access_token_secret)

api = tweepy.API(auth)


def getOptions():
    countOne = 0
    countTwo = 0
    countThree = 0

    for user in tweepy.Cursor(api.followers, screen_name = "TrendDungeon").items():
        print user.screen_name



getOptions()

"""
trendsJSON = api.trends_place(1)
trends = trendsJSON[0]     #json.loads(trendsJSON)

x = random.randint(0,9)
print trends['trends'][x]['name']
"""
"""
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
"""
"""
status =  api.update_status(status ="Test3")
print status.id
"""
