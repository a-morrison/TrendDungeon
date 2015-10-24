"""
    "This class represents the environment for the game
    "Trend Dungeon
"""
import random
import json
from Scenario import Scenario
from Creature import Creature
from Items import Items

locations = ['Witch Hut', 'Cave', 'Crypt', 'Dark Forest', 'Swamp', 'Canyon', 'Cliff', 'Shoppe']
jsonPath = './json/events.json'

class Environment:
    location = ''
    generalText = ""
    flavorText = ""
    currentScenario = None
    creature = None 

    def __init__(self, player):
        self.player = player

    def loadScenario(self, scenario):
        self.currentScenario = scenario

    def saveScenario(self):
        self.scenario.setInitial(generalText)
        self.scenario.setFlavorText(flavorText)
        self.scenario.setOptionOne(option1)
        self.scenario.setOptionTwo(option2)
        self.scenario.setOptionThree(option3)
        self.scenario.setFinishedOne(finished1)
        self.scenario.setFinishedTwo(finished2)
        self.scenario.setFinishedThree(finished3)
        self.scenario.saveToFile()

    def generateScenario(self, trend):
        self.location = random.choice(locations)
        self.getGeneralText(trend)

        encounterChance = randint(0,100)
        self.getFlavorText()
        
        if location == "Shoppe":
            self.shoppeEncouter()
        else:
            if encounterChance <= 20:
                self.exploreRoom()
            elif encounterChance <= 50:
                self.giveItem()
            else:
                self.startEncounter()
    
    def giveItem(self):
        self.scenario.hasItem = True

    def exploreRoom(self):
        
    def startEncounter(self):
        self.spawnCreature()
    
    def shoppeEncounter(self):
        
    def getGeneralText(self, trend):
        with open(jsonPath, "r") as data_file:
            data = json.load(data_file)

        generalText = data[self.location]["generalText"]
        self.generalText = generalText.format(trend)
    
    def getFlavorText(self):
        with open(jsonPath, "r") as data_file:
            data = json.load(data_file)

        length = len(data[self.location]["flavorText"])
        flavorText = data[self.location]["flavorText"][random.randint(0,length-1)
        self.flavorText = flavorText

    def spawCreature(self):
        self.creature = Creature()

    def getNoun(self, trend):
        trend = trend.replace(" ","")
        trendList = list(trend)
        nums = ['1','2','3','4','5','6','7','8','9','0']

        if len(trendList) >= 15:
            temp = list()
            for x in trendList:
                if x.isupper() or x in nums:
                    temp.append(x)
                    trendList = temp;
        if trendList[0] != "#":
            trendList.insert(0,"#")

        trendStr = ''.join(trendList)
        return trendStr
