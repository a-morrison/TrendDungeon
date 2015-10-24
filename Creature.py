import Player
import random

"""
"This class represents a creature for the game
"Trend Dungeon
"""

creatures = ['Dragon','Bear','Wraith','Golem','Skeleton','Werewolf','Ghoul','Undead','Slime']

class Creature:
    self.monster
    self.attack
    self.hp
    
def __init___(self):
        self.monster = random.choice(creatures)
        self.attack = random.random(1,3)+Player.getLevel()
        self.hp = random.random(4,6)+Player.getLevel()
