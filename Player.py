"""
  "This class represents a player for the game
  "Trend Dungeon
"""

import json

class Player:
    level = 0
    health = 0
    experiencePoints = 0
    damage = 0

    def __init__(self):
        self.loadPlayer()

    def loadPlayer(self):
        with open("./json/player.json", "r") as data_file:
            data = json.load(data_file)

        level = data["Player"][0]["level"]
        self.level = int(level)

        health = data["Player"][0]["health"]
        self.health = int(health)

        experiencePoints = data["Player"][0]["experiencePoints"]
        self.experiencePoints = int(experiencePoints)

        damage = data["Player"][0]["damage"]
        self.damage = int(damage)
    
    def savePlayer(self):
        with open("./json/player.json", "r") as data_file:
            data = json.load(data_file)

        tmp = data["Player"][0]["level"]
        data["Player"][0]["level"] = str(self.level)

        tmp = data["Player"][0]["health"]
        data["Player"][0]["health"] = str(self.health)

        tmp = data["Player"][0]["experiencePoints"]
        data["Player"][0]["experiencePoints"] = str(self.experiencePoints)

        tmp = data["Player"][0]["damage"]
        data["Player"][0]["damage"]

        with open("./json/player.json", "w") as data_file:
            data_file.write(json.dumps(data, indent=4, 
                            separators=(', ', ': ')))

    """
      "Returns the health of the player.
    """
    def getHealth(self):
        return self.health
    
    """
      "Removes a supplied number of health
      "points.
      "
      "@param pointsToRemove: number of points
      "removed.
    """
    def removeHealth(self, pointsToRemove):
        self.health -= pointsToRemove
    
    """
      "Give a supplied number of health
      "points.
      "
      "@param: pointsToGive: number of points
      "given.
    """
    def giveHealth(self, pointsToGive):
        self.health += pointsToGive
    
    """
      "Returns the damage amount of the player.
    """
    def getDamage(self):
        return self.damage
    
    """
      "Gives the player a supplied number of
      "experience points.
      "
      "@param pointsToGive: number of points
      "given.
    """
    def giveExperiencePoints(self, pointsToGive):
        self.experiencePoints += pointsToGive

        if self.experiencePoints % 100 == 0:
            self.levelUp()
            
    """
      "Levels up the player.
    """
    def levelUp(self):
        self.level += 1

    def isDead(self):
        if health <= 0:
            return true
        else:
            return false
