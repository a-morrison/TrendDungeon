"""
  "This class represents a player for the game
  "Trend Dungeon
"""

import json
from Items import Items

jsonPath = "./json/player.json"

class Player:
    level = 0
    totalHealth = 0
    currentHealth = 0
    experiencePoints = 0
    damage = 0
    lastID = 1
    item = None

    def __init__(self, jsonPath):
        self.loadPlayer(jsonPath)

    """
      "Loads save data from json file.
    """
    def loadPlayer(self, jsonPath):
        with open(jsonPath, "r") as data_file:
            data = json.load(data_file)

        level = data["Player"][0]["level"]
        self.level = int(level)

        health = data["Player"][0]["totalHealth"]
        self.totalHealth = int(health)

        health = data["Player"][0]["currentHealth"]
        self.currentHealth = int(health)

        experiencePoints = data["Player"][0]["experiencePoints"]
        self.experiencePoints = int(experiencePoints)

        damage = data["Player"][0]["damage"]
        self.damage = int(damage)

        item = data["Player"][0]["item"]
        self.item = Items(item)

        lastID = data["Player"][0]["lastID"]
        self.lastID = int(lastID)

    """
      "Writes player data to json file.
    """
    def savePlayer(self):
        with open(jsonPath, "r") as data_file:
            data = json.load(data_file)

        tmp = data["Player"][0]["level"]
        data["Player"][0]["level"] = str(self.level)

        tmp = data["Player"][0]["totalHealth"]
        data["Player"][0]["totalHealth"] = str(self.totalHealth)

        tmp = data["Player"][0]["currentHealth"]
        data["Player"][0]["currentHealth"] = str(self.currentHealth)

        tmp = data["Player"][0]["experiencePoints"]
        data["Player"][0]["experiencePoints"] = str(self.experiencePoints)

        tmp = data["Player"][0]["damage"]
        data["Player"][0]["damage"] = str(self.damage)

        tmp = data["Player"][0]["item"]
        data["Player"][0]["item"] = self.item.toJSON()

        tmp = data["Player"][0]["lastID"]
        data["Player"][0]["lastID"] = str(self.lastID)

        with open(jsonPath, "w") as data_file:
            data_file.write(json.dumps(data, indent=4,
                            separators=(', ', ': ')))

    """
      "Returns the health of the player.
    """
    def getHealth(self):
        return self.currentHealth

    """
      "Removes a supplied number of health
      "points.
      "
      "@param pointsToRemove: number of points
      "removed.
    """
    def removeHealth(self, pointsToRemove):
        self.currentHealth -= pointsToRemove
        if self.currentHealth <= 0:
            self.currentHealth = 0

    """
      "Give a supplied number of health
      "points.
      "
      "@param: pointsToGive: number of points
      "given.
    """
    def giveHealth(self, pointsToGive):
        self.currentHealth += pointsToGive
        if self.currentHealth >= self.totalHealth:
            self.currentHealth = self.totalHealth

    """
      "Returns the damage amount of the player.
    """
    def getDamage(self):
        if item == 0:
            return self.damage
        else:
            return item.damage * self.damage

    """
      "Gives the player a supplied number of
      "experience points.
      "
      "@param pointsToGive: number of points
      "given.
    """
    def giveExperiencePoints(self, pointsToGive):
        self.experiencePoints += pointsToGive

        if self.experiencePoints / 100 > 0:
            self.levelUp()

    """
      "Levels up the player.
    """
    def levelUp(self):
        self.level += 1
        self.totalHealth += 1
        self.giveHealth(self.totalHealth)
        self.experiencePoints = 0

    """
      "Returns the player's level.
    """
    def getLevel(self):
        return self.level

    """
      "Returns true if the player is dead.
    """
    def isDead(self):
        if self.currentHealth <= 0:
            return True
        else:
            return False
