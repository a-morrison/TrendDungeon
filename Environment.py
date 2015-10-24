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
        trendList = list(trend)
        if trendList[0] != '#':
            trendList[0] = '#'
        trendStr = ''.join(trendList)
        return trendStr
