import random

elements = ['Fire','Frost','Ground', 'Ether', 'Lightning']
materials = ['Iron','Gem','Oak','Bone','Air']
itemTypes = ['Sword','Crystal','Hammer','Bow','Lute']

"""
Item class for weapons that the player can have
"""
class Items:
    name = ""
    damage = 0
    def __init__(self):
        elem = random.choice(elements)
        mat = random.choice(materials)
        item = random.choice(itemTypes)

        self.name = "{} {} of {}".format(mat,item,elem)
        self.damage = random.randint(0,3)

    def toJSON(self):
        return {'name':self.name,'damage':self.damage}
