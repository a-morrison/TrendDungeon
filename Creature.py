import Player
import random

"""
"This class represents a creature for the game
"Trend Dungeon
"""

lowtier = ['Slime','Bear','Undead','Bat']
midtier = ['Skeleton','Werewolf','Ghoul']
hightier = ['Dragon','Wraith','Golem']
class Creature:
    self.monster
    self.attack
    self.hp
    
def __init___(self):
    if Player.getLevel() <= 5:
        self.monster = random.choice(lowtier)
    elif Player.getLevel() <=10:
        self.monster = random.choice(midtier)
    else:
        self.monster = random.choice(hightier)
        
    self.attack = random.random(1,3)+Player.getLevel()
    self.hp = random.random(3,6)+Player.getLevel()
