"""
    "This class represents the environment for the game
    "Trend Dungeon
"""
import random
import json
from Scenario import Scenario
from Creature import Creature
from Items import Items

locations = ['Witch Hut', 'Cave', 'Crypt', 'Dark Forest', 'Swamp', 'Canyon', 'Cliff', 'Castle', 'Graveyard', 'Shoppe']
jsonPath = './json/events.json'

class Environment:
    location = ""
    trend = ""
    generalText = ""
    flavorText = ""
    option1 = ""
    option2 = ""
    option3 = ""
    finished1 = [None,None,None,None]
    finished2 = [None,None,None,None]
    finished3 = [None,None,None,None]
    scenario = None
    creature = None

    def __init__(self, trend):
        self.trend = trend
        self.scenario = Scenario()

    def loadScenario(self, scenario):
        self.currentScenario = scenario

    def saveScenario(self):
        self.scenario.setInitial(self.generalText)
        self.scenario.setFlavorText(self.flavorText)
        self.scenario.setOptionOne(self.option1)
        self.scenario.setOptionTwo(self.option2)
        self.scenario.setOptionThree(self.option3)
        self.scenario.setFinishedOne(self.finished1)
        self.scenario.setFinishedTwo(self.finished2)
        self.scenario.setFinishedThree(self.finished3)
        #self.scenario.setCreature(self.creature)
        self.scenario.saveToFile()
        
    def generateScenario(self, trend):
        self.location = random.choice(locations)
        self.getGeneralText(trend)

        encounterChance = random.randint(0,100)
        self.flavorText = self.getFlavorText()

        if self.location == "Shoppe":
            self.shoppeEncounter()
        else:
            if encounterChance <= 20:
                self.exploreRoom()
            elif encounterChance <= 50:
                self.giveItem()
            else:
                self.startEncounter()
        return self

    def giveItem(self):
        self.scenario.hasItem = True
        self.finished1[0] = "You recieved an item!"
        self.finished1[1] = True
        self.finished1[2] = 0
        self.finished1[3] = 0

        self.finished2[0] = "You passed on an item!"
        self.finished2[1] = False
        self.finished2[2] = 0
        self.finished2[3] = 0

        self.option1 = "Leave"

    def exploreRoom(self):
        self.option1 = "Leave"
        addedText = self.getFlavorText()

        while addedText == self.flavorText:
            addedText = self.getFlavorText()

        self.flavorText = self.flavorText
        self.finished1[0]=("You leave the {}.".format(self.location))
        self.finished1[1]=(True)
        self.finished1[2]=(0)
        self.finished1[3]=(0)

    def startEncounter(self):
        self.spawnCreature()

        self.option1 = "Fight"
        self.option2 = "Flee"

        self.setEncounterOptionOne()
        self.setEncounterOptionTwo()

    def getCurrentCreatureHealth(self):
        return self.creature.getCreatureHealth()

    def setEncounterOptionOne(self):
        self.finished1[0] = "You defeat the {}!".format(self.creature.getCreatureType())
        self.finished1[1]=(True)
        self.finished1[2]=(20)
        self.finished1[3]=(self.creature.getCreatureDamage())

    def setEncounterOptionTwo(self):
        self.finished2[0]=("You attempt to flee from the {}!".format(self.creature.getCreatureType()))
        self.finished2[1]=(False)
        self.finished2[2]=(0)
        self.finished2[3]=(self.creature.getCreatureDamage())

    def shoppeEncounter(self):
        self.option1 = "Take Item"
        self.option2 = "Leave"
        addedText = self.getFlavorText()

        while addedText == self.flavorText:
            addedText = self.getFlavorText()

        self.flavorText = self.flavorText
        self.finished1[0] = "You leave the {}.".format(self.location)
        self.finished2[0] = "You leave the {}.".format(self.location)
        self.finished1[1]=(True)
        self.finished1[2]=(0)
        self.finished1[3]=(0)
        
        self.finished2[1]=(False)
        self.finished2[2]=(0)
        self.finished2[3]=(0)

    def getGeneralText(self, trend):
        with open(jsonPath, "r") as data_file:
            data = json.load(data_file)

        generalText = data[self.location]["generalText"]
        self.generalText = generalText.format(trend)

    def getFlavorText(self):
        with open(jsonPath, "r") as data_file:
            data = json.load(data_file)

        length = len(data[self.location]["flavorText"])
        flavorText = data[self.location]["flavorText"][random.randint(0,length-1)]
        return flavorText

    def spawnCreature(self):
        self.creature = Creature()
        self.scenario.setCreature(self.creature)

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
