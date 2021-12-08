from random import randint
from dataclasses import dataclass

@dataclass
class Drop:

    inventory : dict
    attack : int
    potion : int

    def __post_init__(self):
        self.drop_items()

    def drop_items(self):
        dict = {"EXCALIBUR" : 50, "Hâche": 20, "Epee": 15, "Dague": 8, "Cure-dent": 2}
        chance = randint(0, 100)
        values = list(self.inventory.values())
        keys = list(self.inventory.keys())
        for i in range (len(self.inventory.keys())-1, -1, -1):
            if chance < values[i]:
                if keys[i] == "Potion":
                    self.potion += 1
                else:
                    self.attack += dict[keys[i]]
                break
        return self.attack, self.potion