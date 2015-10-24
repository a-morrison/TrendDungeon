import nltk

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
