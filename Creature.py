import Player
import random

"""
"This class represents a creature for the game
"Trend Dungeon
"""

lowtier = ['Rat','Slime','Goblin','Undead','Bat']
midtier = ['Skeleton','Werewolf','Ghoul','Spider','Orc']
hightier = ['Dragon','Wraith','Golem','Shade','Warlock']

class Creature:
    monster = ""
    attack = 0
    hp = 0
    
    def __init__(self):
        if Player.getLevel() <= 5:
            self.monster = random.choice(lowtier)
        elif Player.getLevel() <=10:
            self.monster = random.choice(midtier)
        else:
            self.monster = random.choice(hightier)
            
        self.attack = random.random(1,3)+Player.getLevel()
        self.hp = random.random(3,6)+Player.getLevel()

    def getCreautreType(self):
        return str(self.monster)

    def setCreatureType(self, monster):
        self.monster = monster

    def getCreatureHealth(self):
        return int(self.hp)

    def setCreatureHealth(self, healthPoints):
        self.hp = healthPoints

    def getCreatureDamage(self):
        return int(self.attack)

    def setCreatureDamage(self, damage):
        self.attack = damage
