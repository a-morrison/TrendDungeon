import random

elements = ['Fire','Frost','Ground', 'Ether', 'Lightning']
materials = ['Iron','Gem','Oak','Bone','Air']
itemTypes = ['Sword','Crystal','Hammer','Bow','Lute']

"""
Item class for weapons that the player can have
"""
class Item:
    self.name
    self.damage
    def __init__(self):
        elem = random.choice(elements)
        mat = random.choice(materials)
        item = random.choice(itemTypes)

        self.name = "{} {} of {}".format(mat,item,elem)
        self.damage = random.random(0,3)