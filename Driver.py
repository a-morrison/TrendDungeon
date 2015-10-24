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
        self.trend = self.getTrend()
        self.scen = Enviroment.scenerio(self.trend)

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
        api.update_status(status = scen)

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
