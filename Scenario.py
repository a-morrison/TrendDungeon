"""
  "This class represents a scenario for the game
  "Trend Dungeon.
"""

import json

jsonPath = "./json/scenario.json"

class Scenario:
    self.initial = ""
    self.option1 = ""
    self.option2 = ""
    self.option3 = ""
    self.finished1 = ""
    self.finished2 = ""
    self.finished = False

    def __init__(self):
        self.loadFromFile(jsonPath)

    def loadFromFile(self, jsonFile):
        with open(jsonFile, "r") as data_file:
            data = json.load(data_file)

        initial = data["Scenario"][0]["initial"]

        option1 = data["Scenario"][0]["option1"]

        option2 = data["Scenario"][0]["option2"]

        option3 = data["Scenario"][0]["option3"]
    
    def saveToFile(self, jsonFile): 

    def getOption(self, optionNumber):
