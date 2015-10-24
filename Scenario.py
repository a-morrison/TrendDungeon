"""
  "This class represents a scenario for the game
  "Trend Dungeon.
"""

import json
import Creature
import random

jsonPath = "./json/scenario.json"

class Scenario:
    initial = ""
    falvorText = ""
    creature = None
    option1 = ""
    option2 = ""
    option3 = ""
    finish1 = [0,0,0,0]
    finish2 = [0,0,0,0]
    finish3 = [0,0,0,0]
    finished = False
    hasItem = False

    def __init__(self):
        self.loadFromFile(jsonPath)

    def loadFromFile(self, jsonFile):
        with open(jsonFile, "r") as data_file:
            data = json.load(data_file)

        initial = data["Scenario"][0]["initial"]
        self.initial = str(initial)

        flavor = data["Scenario"][0]["flavorText"]
        self.flavorText = str(flavor)

        option1 = data["Scenario"][0]["option1"]
        self.option1 = str(option1)

        option2 = data["Scenario"][0]["option2"]
        self.option2 = str(option2)

        option3 = data["Scenario"][0]["option3"]
        self.option3 = str(option3)

        finish1 = data["Scenario"][0]["finish1"]
        self.finish1 = (list)(finish1)

        finish2 = data["Scenario"][0]["finish2"]
        self.finish2 = (list)(finish2)

        finish3 = data["Scenario"][0]["finish3"]
        self.finish3 = (list)(finish3)

        finished = data["Scenario"][0]["finished"]
        self.finished = bool(finished)

        self.loadCreature()

    def saveToFile(self):
        with open(jsonPath, "r") as data_file:
            data = json.load(data_file)

        tmp = data["Scenario"][0]["initial"]
        data["Scenario"][0]["initial"] = str(self.initial)

        tmp = data["Scenario"][0]["flavorText"]
        data["Scenario"][0]["flavorText"] = str(self.flavorText)

        tmp = data["Scenario"][0]["option1"]
        data["Scenario"][0]["option1"] = str(self.option1)

        tmp = data["Scenario"][0]["option2"]
        data["Scenario"][0]["option2"] = str(self.option2)

        tmp = data["Scenario"][0]["option3"]
        data["Scenario"][0]["option3"] = str(self.option3)

        tmp = data["Scenario"][0]["finish1"]
        data["Scenario"][0]["finish1"] = self.finish1

        tmp = data["Scenario"][0]["finish2"]
        data["Scenario"][0]["finish2"] = self.finish2

        tmp = data["Scenario"][0]["finish3"]
        data["Scenario"][0]["finish3"] = self.finish3

        tmp = data["Scenario"][0]["finished"]
        data["Scenario"][0]["finished"] = self.finished

        with open(jsonPath, "w") as data_file:
            data_file.write(json.dumps(data, indent=4,
                            separators=(', ', ': ')))

        self.saveCreature()

    def loadCreature(self):
        with open(jsonPath, "r") as data_file:
            data = json.load(data_file)

        creatureType = data["Scenario"][0]["creature"]["type"]
        creatureHealth = data["Scenario"][0]["creature"]["health"]
        creatureDamage = data["Scenario"][0]["creature"]["damage"]

        if creatureType != None:
            self.creature.setCreatureType(creatureType)
            self.creature.setCreatureHealth(int(creatureHealth))
            self.creature.setCreatureDamage(int(creatureDamage))

    def saveCreature(self):
        if self.creature == None:
            return None

        with open(jsonPath, "r") as data_file:
            data = json.load(data_file)

        tmp = data["Scenario"][0]["creature"]["type"]
        data["Scenario"][0]["creature"]["type"] = str(self.creature.getCreatureType)

        tmp = data["Scenario"][0]["creature"]["health"]
        data["Scenario"][0]["creature"]["health"] = int(self.creature.getCreatureHealth)

        tmp = data["Scenario"][0]["creature"]["damage"]
        data["Scenario"][0]["creature"]["damage"] = int(self.creature.getCreatureDamage)

        with open(jsonPath, "w") as data_file:
            data_file.write(json.dumps(data, indent=4,
                            separators=(', ', ': ')))

    def setCreature(self, creature):
        self.creature = creature

    def getEncounterText(self):
        x = random.randint(0,len(self.flavorText)-1)
        encounterText = self.initial + " " + self.flavorText[x]
        return encounterText

    def setInitial(self, newInitial):
        self.initial = newInitial

    def getInitial(self):
        return self.initial

    def setFlavorText(self, newText):
        self.flavorText = newText

    def getFlavorText(self):
        return self.flavorText

    def setOptionOne(self, newOption):
        self.option1 = newOption

    def setOptionTwo(self, newOption):
        self.option2 = newOption

    def setOptionThree(self, newOption):
        self.option3 = newOption

    def getOption(self, optionNumber):
        if optionNumber == 1:
            return self.option1
        elif optionNumber == 2:
            return self.option2
        else:
            return self.option3

    def setFinishedOne(self, newFinished):
        self.finish1 = newFinished

    def setFinishedTwo(self, newFinished):
        self.finish2 = newFinished

    def setFinishedThree(self, newFinished):
        self.finish3 = newFinished

    def getFinished(self, finishedNumber):
        if finishedNumber == 1:
            return self.finish1
        elif finishedNumber == 2:
            return self.finish2
        else:
            return self.finish3

    def isFinished(self):
        return self.finished

    def playerHasItem(self):
        return self.hasItem;
