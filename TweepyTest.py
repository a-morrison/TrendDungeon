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

    return random.choice([1,2,3])

    for tweet in tweepy.Cursor(api.user_timeline, screen_name = "TrendDungeon").items():
        print tweet.text
        print tweet.in_reply_to_user_screen_name
        if tweet.in_reply_to_user_screen_name == "@TrendDungeon":
            print tweet.text
            if tweet.text.find('#1')>=0:
                countOne+=1
                break
            elif tweet.text.find('#2')>=0:
                countTwo+=1
                break
            elif tweet.text.find('#3')>=0:
                countThree+=1
                break
        break

    if countOne>countTwo and countOne>countThree:
        return 1
    elif countTwo>countThree:
        return 2
    else:
        return 3

print getOptions()

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
