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
        self.initial = str(initial)

        option1 = data["Scenario"][0]["option1"]
        self.option1 = str(option1)

        option2 = data["Scenario"][0]["option2"]
        self.option2 = str(option2)

        option3 = data["Scenario"][0]["option3"]
        self.option3 = str(option3)

        finished1 = data["Scenario"][0]["finished1"]
        self.finished1 = str(finished1)

        finished2 = data["Scenario"][0]["finished2"]
        self.finished2 = str(finished2)

        finished = data["Scenario"][0]["finished"]
        self.finished = bool(finished)
    
    def saveToFile(self): 
        with open(jsonPath, "r") as data_file:
            data = json.load(data_file)

        tmp = data["Scenario"][0]["initial"]
        data["Scenario"][0]["initial"] = str(self.initial)

        tmp = data["Scenario"][0]["option1"]
        data["Scenario"][0]["option1"] = str(self.option1)

        tmp = data["Scenario"][0]["option2"]
        data["Scenario"][0]["option2"] = str(self.option2)

        tmp = data["Scenario"][0]["option3"]
        data["Scenario"][0]["option3"] = str(self.option3)

        tmp = data["Scenario"][0]["finished1"]
        data["Scenario"][0]["finished1"] = str(self.finished1)

        tmp = data["Scenario"][0]["finished2"]
        data["Scenario"][0]["finished2"] = str(self.finished2)

        tmp = data["Scenario"][0]["finished"]
        data["Scenario"][0]["finished"] = str(self.finished)
        
        with open(jsonPath, "w") as data_file:
            data_file.write(json.dumps(data, indent=4,
                            separators=(', ', ': ')))

    def getOption(self, optionNumber):
