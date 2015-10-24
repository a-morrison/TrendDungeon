"""
    "This class represents the environment for the game
    "Trend Dungeon
"""
import random
from Scenario import Scenario
from Creature import Creature

locations = ['Witch Hut', 'Cave', 'Crypt', 'Dark Forest', 'Swamp', 'Canyon', 'Cliff', 'Shoppe']
jsonPath = './json/events.json'

class Environment:
    location = ''
    generalText = ""
    newScenario = None
    creature = None 

    def __init__(self):
        newScenario = ""

    def loadScenario(self, scenario):

    def saveScenario(self, scenario):

    def generateScenario(self, trend):
        self.location = random.choice(locations)
        self.getGeneralText(trend)

    def getGeneralText(self, trend):
        with open(jsonPath, "r") as data_file:
            data = json.load(data_file)

        generalText = data[self.location][0]["generalText"]
        self.generalText = generalText.format(trend)

    def spawCreature(self):
        self.creature = Creature()

    def getNoun(self, trend):
        trendList = list(trend)
        for x in trendList:
            if x.isupper():
                for y in trendList:
                    if y.isupper() and y != x:
                        trendList[x:y-1]
        if trendList[0] != '#':
            trendList[0] = '#'
        trendStr = ''.join(trendList)
        return trendStr
