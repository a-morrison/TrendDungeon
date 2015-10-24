import tweepy
import Passwords as passwords
from Player import Player
from Environment import Environment
from Scenario import Scenario
from Items import Items
import json
import time
import random


sleepTime = 2
savedPlayerJSON = './json/player.json'
savedScenJSON = './json/scenario.json'

"""
API initialization for the bot
"""
auth = tweepy.OAuthHandler(passwords.apiKey, passwords.apiSecret)

auth.set_access_token(passwords.access_token, passwords.access_token_secret)

api = tweepy.API(auth)


def getReplies(lastID):
    countOne = 0
    countTwo = 0
    countThree = 0

    return random.choice([1,2,3])

    for user in tweepy.Cursor(api.followers, screen_name = "TrendDungeon").items():
        for tweet in tweepy.Cursor(api.user_timeline, screen_name= user.screen_name, count = 20, since_id=lastID).items():
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


"""
  "This class represents a driver for the game
  "Trend Dungeon.
"""

class Driver:
    p = None         #the player
    trend = ""     #the Trending topic
    scen = None     #the scenerio to do next
    """
    Constructor
    """
    def __init__(self):
        self.p = Player(savedPlayerJSON)
        #self.updatePlayer(self.p,True,0,0)
        if self.p.isDead():
            self.p = Player("./json/newPlayerTemplate")
        self.trend = getTrend()
        #print self.trend
        self.scen = Scenario()
        self.scen.loadFromFile(savedScenJSON)
        if self.scen.finished or self.scen.initial == None:
            self.followUpTweet(getReplies(self.p.lastID))
            item = self.scen.getItem()
            exp = self.scen.amountXP()
            health = self.scen.amountHealth()
            updatePlayer(self.p,item,exp,health)
            self.scen = Enviroment.generateScenerio(self.trend)
            self.scen.saveToFile()


    def updatePlayer(self,player,item,exp,health):
        if item:
            player.item = Items(None)
        player.giveExperiencePoints(exp)
        if health>0:
            player.giveHealth(health)
        else:
            player.removeHealth(health)
        player.savePlayer()

    """
    Method to post the Announce Tweet using API
    """
    def announceTweet(self):
        msg = "The trend for this encounter is {}! Prepare for adventure!"
        msg = msg.format(self.trend)
        print msg #api.update_status(status = msg)
        time.sleep(sleepTime)

    """
    Method to post the Scenario Tweet using API
    """
    def scenarioTweet(self):
        msg = self.scen.getInitial()
        print msg #api.update_status(status = msg)
        time.sleep(sleepTime)

    """
    Method to post the Status Tweet using API
    """
    def statusTweet(self):
        msg = "You have {0.currentHealth} Health, {0.experiencePoints} XP, and are level {0.level}."
        if self.p.item.name != "":
            msg+=" You currently have the {0.item.name} Item."
        msg = msg.format(self.p)
        print msg #api.update_status(status = msg)
        time.sleep(sleepTime)

    """
    Method to post the Option Tweet using API
    """
    def optionsTweet(self):
        temp = self.scen.getEncounterText()
        msg = "{1} Follow and reply with #1 to {0.option1}"
        if self.scen.option2 != None:
            msg+=", #2 to {0.option2}"
        else:
            msg+="!"
        if self.scen.option3 != None:
            msg+=" , or #3 to {0.option3}!"
        else:
            msg+= "!"
        msg = msg.format(self.scen,temp)
        self.scen.finished = True
        print msg
        #return api.update_status(status = msg)
        time.sleep(sleepTime)

    def followUpTweet(self, option):
        msg = "{}"
        msg.format(self.scen.getFinished(option))
        print msg #api.update_status(status = msg)
        time.sleep(sleepTime)

"""
Method to get the random trend to use on this run
"""
def getTrend():
    trendsJSON = api.trends_place(23424977)
    trends = trendsJSON[0]
    x = random.randint(0,9)
    trend = trends['trends'][x]['name'].encode('utf-8','ignore')
    print trend
    return trend


def main():
    driver = Driver()
    driver.announceTweet()
    driver.scenarioTweet()
    driver.statusTweet()
    driver.optionsTweet()
    driver.p.lastID = 1 #driver.optionsTweet().id
    driver.p.savePlayer()
    driver.scen.saveToFile()

main()
