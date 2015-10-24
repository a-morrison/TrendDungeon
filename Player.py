"""
  "This class represents a player for the game
  "Trend Dungeon
"""
class Player:
    level = 1
    health = 10
    experiencePoints = 0
    damage = 1

    def __init__(self):
    
    """
      "Returns the health of the player.
    """
    def getHealth(self):
        return health
    
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
        return damage
    
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
    def levelUp(self)
        self.level += 1

    
