import nltk

"""
    "This class represents the environment for the game
    "Trend Dungeon
"""
from Scenario import Scenario

locations = ['Cave', 'Crypt', 'Dark Forest', 'Swamp', 'Canyon','Cliff', 'Witche\'s Hut', 'Shoppe']

class Environment:

    def __init__(self):

    def loadScenario(self, scenario):

    def saveScenario(self, scenario):

    def generateScenario(self, trend):
        
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
