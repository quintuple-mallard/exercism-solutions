import random as rd
class Character:
    def __init__(self):
        rolls = [rd.randint(1,6),rd.randint(1,6),rd.randint(1,6),rd.randint(1,6)]
        rolls.remove(min(rolls))
        self.strength=sum(rolls)
        rolls = [rd.randint(1,6),rd.randint(1,6),rd.randint(1,6),rd.randint(1,6)]
        rolls.remove(min(rolls))
        self.dexterity=sum(rolls)
        rolls = [rd.randint(1,6),rd.randint(1,6),rd.randint(1,6),rd.randint(1,6)]
        rolls.remove(min(rolls))
        self.constitution=sum(rolls)
        rolls = [rd.randint(1,6),rd.randint(1,6),rd.randint(1,6),rd.randint(1,6)]
        rolls.remove(min(rolls))
        self.intelligence=sum(rolls)
        rolls = [rd.randint(1,6),rd.randint(1,6),rd.randint(1,6),rd.randint(1,6)]
        rolls.remove(min(rolls))
        self.wisdom=sum(rolls)
        rolls = [rd.randint(1,6),rd.randint(1,6),rd.randint(1,6),rd.randint(1,6)]
        rolls.remove(min(rolls))
        self.charisma=sum(rolls)
        self.hitpoints=10+modifier(self.constitution)
    def ability(self):
        ability_idx=rd.randint(0,5)
        return self.strength
def modifier(value):
    return (value-10)//2