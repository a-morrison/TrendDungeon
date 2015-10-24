import tweepy
import Passwords as passwords
import Player
import Enviroment
import json


"""
API initialization for the bot
"""
auth = tweepy.OAuthHandler(passwords.apiKey, passwords.apiSecret)

auth.set_access_token(passwords.access_token, passwords.access_token_secret)

api = tweepy.API(auth)


def getOptions():
    countOne = 0;
    countTwo = 0;
    countThree = 0;
    for user in tweepy.Cursor(api.followers, screen_name = "TrendDungeon").items():
        for tweet in tweepy.Cursor(api.user_timeline, screen_name= user.screen_name, count = 20).items():
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
        return 1;
    elif countTwo>countThree:
        return 2
    else:
        return 3


"""
  "This class represents a driver for the game
  "Trend Dungeon.
"""

class Driver:
    self.p          #the player
    self.trend      #the Trending topic
    self.scen       #the scenerio to do next
    """
    Constructor
    """
    def __init__(self):
        self.p = Player.loadPlayer()
        if p.isDead:
            p = Player("./json/newPlayerTemplate")
        self.trend = self.getTrend()
        self.scen = Enviroment.loadScenario()
        if self.scen.finished:
            followUpTweet(self,getOption())
            self.scen = Enviroment.generateScenerio(self.trend)
            Enviroment.saveScenario(scen)

    """
    Method to get the random trend to use on this run
    """
    def getTrend():
        trendsJSON = api.trends_place(1)
        trends = trendsJSON[0]
        x = random.randint(0,9)
        return trends['trends'][x]['name']

    """
    Method to post the Announce Tweet using API
    """
    def announceTweet(self):
        msg = "The trend for this encounter is {}! Prepare for adventure!"
        msg.format(self.trend)
        api.update_status(status = msg)

    """
    Method to post the Scenario Tweet using API
    """
    def scenarioTweet(self):
        msg = scen.initial
        api.update_status(status = msg)

    """
    Method to post the Status Tweet using API
    """
    def statusTweet(self):
        msg = "You have {0.health} Health, {0.experiencePoints} XP, and are level {0.level}. You currently have the {0.item} Item."
        msg.format(self.p)
        api.update_status(status = msg)

    """
    Method to post the Option Tweet using API
    """
    def optionsTweet(self):
        msg = "Follow and reply with #1 to {0.option1} or #2 to {0.option2}!"
        msg.format(scen)
        api.update_status(status = msg)

    def followUpTweet(self, option):
        msg = "{}"
        msg.format(scen.getOption(option))
        api.update_status(status = msg)

def main():
    driver = Driver()
    driver.announceTweet()
    driver.scenarioTweet()
    driver.statusTweet()
    driver.optionsTweet()
