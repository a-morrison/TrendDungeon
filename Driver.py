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

    return 1

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

    if countOne>=countTwo and countOne>=countThree:
        return 1
    elif countTwo>=countThree:
        return 2
    else:
        return 3


def loadScenFromFile(jsonFile):
    s = Scenario()
    with open(jsonFile, "r") as data_file:
        data = json.load(data_file)

    initial = data["Scenario"][0]["initial"]
    s.initial = str(initial)

    flavor = data["Scenario"][0]["flavorText"]
    s.flavorText = str(flavor)

    option1 = data["Scenario"][0]["option1"]
    s.option1 = str(option1)

    option2 = data["Scenario"][0]["option2"]
    s.option2 = str(option2)

    option3 = data["Scenario"][0]["option3"]
    s.option3 = str(option3)

    finish1 = data["Scenario"][0]["finish1"]
    s.finish1 = finish1

    finish2 = data["Scenario"][0]["finish2"]
    s.finish2 = finish2

    finish3 = data["Scenario"][0]["finish3"]
    s.finish3 = finish3

    finished = data["Scenario"][0]["finished"]
    s.finished = bool(finished)

    s.loadCreature()

    return s

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
        if self.scen.finished:
            option = getReplies(self.p.lastID)
            self.followUpTweet(option)
            if option == 1:
                item = self.scen.finish1[1]
                exp = self.scen.finish1[2]
                health = self.scen.finish1[3]
            elif option ==2:
                item = self.scen.finish2[1]
                exp = self.scen.finish2[2]
                health = self.scen.finish2[3]
            else:
                item = self.scen.finish3[1]
                exp = self.scen.finish3[2]
                health = self.scen.finish3[3]
            self.updatePlayer(self.p,item,exp,health)
        tempEnviro = Environment(self.trend)
        tempEnviro.generateScenario(self.trend).saveScenario()
        self.scen = loadScenFromFile(savedScenJSON)


    def updatePlayer(self,player,item,exp,health):
        #print item , exp, health
        if item:
            player.item = Items(None)
        player.giveExperiencePoints(int(exp)/int(player.level))
        if health>0:
            player.giveHealth(int(health))
        else:
            player.removeHealth(int(health))
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
        if self.scen.option2 != "":
            msg+=", #2 to {0.option2}"
        if self.scen.option3 != "":
            msg+=" , or #3 to {0.option3}"
        msg+= "!"
        msg = msg.format(self.scen,temp)
        self.scen.finished = True
        print msg
        #return api.update_status(status = msg)
        time.sleep(sleepTime)

    def followUpTweet(self, option):
        msg = "{}"
        temp = self.scen.getFinished(option)[0]
        msg = msg.format(temp)
        msg2 = " You have {0.currentHealth} Health, {0.experiencePoints} XP, and are level {0.level}."
        if self.p.item.name != "":
            msg2+=" You currently have the {0.item.name} Item."
        msg2 = msg2.format(self.p)
        msg += msg2
        print msg #api.update_status(status = msg)
        time.sleep(sleepTime)

"""
Method to get the random trend to use on this run
"""
def getTrend():
    return 'trend'
    trendsJSON = api.trends_place(23424977)
    trends = trendsJSON[0]
    x = random.randint(0,9)
    trend = trends['trends'][x]['name'].encode('utf-8','ignore')
    trend = Environment(trend).getNoun(trend)
    print trend
    return trend


def main():
    driver = Driver()
    #driver.announceTweet()
    #driver.scenarioTweet()
    driver.optionsTweet()
    #driver.statusTweet()
    driver.p.lastID = 1 #driver.optionsTweet().id
    driver.p.savePlayer()
    driver.scen.saveToFile()

main()
