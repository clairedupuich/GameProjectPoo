from dataclasses import dataclass
from typing import ClassVar
from abc import ABCMeta, abstractmethod
from random import randint
from drop import Drop

@dataclass
class Entity(metaclass = ABCMeta):
    
    name : str
    hp : int
    hp_max : int
    strength : int

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def death(self):
        pass

@dataclass
class Monster(Entity):

    points : ClassVar[int]
    droprate : ClassVar[float]
    weak_attack : ClassVar[float]
    defense : int = 0

    def level(self,floor,difficulty):
        """ This function give the force and the health points of the monster, using the floor's level and the difficulty's level."""
        droprate_base = 10
        points_base = 10

        self.droprate = droprate_base * (((floor/10)+difficulty)+1)
        self.strength = round(self.strength * (((floor/10)+difficulty)+1))
        self.hp = round(self.hp * (((floor/10)+difficulty)+1))
        self.points = round(points_base * (((floor/10)+difficulty)+1))
        print(f"{self.name} vient d'apparaître ! Un monstre avec {self.hp} points de vie et avec une force de {self.strength}.")
        return self.points, self.droprate, self.strength, self.hp

    def attack(self,player):
        """This function takes away health points from life's player when an ennemy attacks him."""
        if player.defense != 0 :
            self.weak_attack = round(self.strength / 1.5)
            player.defense -= 1
            player.hp -= self.weak_attack
            print(f"Vous avez subi {self.weak_attack} points de dégâts de la part du {self.name}")
            
        else:    
            player.hp -= self.strength
            print(f"Vous avez subi {self.strength} points de dégâts de la part du {self.name}")
            
        print(f'Il vous reste {player.hp} points de vie.')
        return player.hp


    def death(self, player, score):
        """"This function will delete the last summoned monster and run the drop() method"""
        print(f"Félicitations ! Vous avez réussi à vaincre {self.name}!")
        if self.droprate >= randint(0,100):
            item = {"Dague" : 20, "Potion": 50, "Cure-dent": 30 } 
            dropped = Drop(item, player.strength, player.potion)
            player.strength, player.potion = dropped.drop_items()
        score += self.points
        return score

class Boss(Entity):

    points : ClassVar[int]
    droprate : ClassVar[float]
    weak_attack : ClassVar[float]
    defense : ClassVar[int] = 0

    def level(self,floor,difficulty):
        """ This function give the force and the health points of the boss, using the floor's level and the difficulty's level."""
        droprate_base = 15
        points_base = 15

        self.droprate = droprate_base * (((floor/10)+difficulty)+1)
        self.strength = round(self.strength * (((floor/10)+difficulty)+1))
        self.hp = round(self.hp * (((floor/10)+difficulty)+1))
        self.points = round(points_base * (((floor/10)+difficulty)+1))
        print(f"{self.name} vient d'apparaître ! Un boss avec {self.hp} points de vie et avec une force de {self.strength}.")
        return self.points, self.droprate, self.strength, self.hp

    def attack(self,player):
        """This function takes away health points from life's player when the Boss attacks him."""
        if player.defense != 0 :
            self.weak_attack = round(self.strength / 1.5)
            player.defense -= 1
            player.hp -= self.weak_attack
            print(f"Vous avez subi {self.weak_attack} points de dégâts de la part du {self.name}")

        else:    
            player.hp -= self.strength
            print(f"Vous avez subi {self.strength} points de dégâts de la part du {self.name}")
            print(f'Il vous reste {player.hp} points de vie.')
            # Come back to the fight
        return player.hp

    def death(self, player, score):
        """"This function will delete the last summoned monster and run the drop() method"""
        print(f"Félicitations ! Vous avez réussi à vaincre {self.name}!")
        if self.droprate >= randint(0,100):
            item = {"Excalibur" : 1, "Hâche": 49, "Epee": 30, "Potion": 20 } 
            dropped = Drop(item, player.strength, player.potion)
            player.strength, player.potion = dropped.drop_items()
        score += self.points
        return score
    
    def defend(self):
        """This function give a protection to the Boss during 3 turns."""
        self.defense = 3
        print(f"{self.name} vient de s'équiper d'une protection pendant 3 tours !")
        # Come back to the fight
        return self.defense

@dataclass
class Player(Entity):
    
    potion : ClassVar[int] = 3
    defense : ClassVar[int] = 0
        
    def attack(self,monster,score):
        """This function takes away health points from life's ennemy when the player attacks."""
        if monster.hp <= self.strength:
            score = monster.death(self, score)
            print(f"Votre score est de {score}")
            monster.hp = 0
        else:
            if monster.defense == 0:
                monster.hp -= self.strength
            else:
                monster.hp -= round(self.strength/1.5)
            print(f'Il reste {monster.hp} PV à l\'ennemi')
            # Retour sur combat
        return score, monster.hp
    
    def death(self):
        return False
    
    def defend(self):
        """This function give a shield to the player during 3 turns."""
        if self.defense !=0 :
            print("Tu as déjà un bouclier !")
        else:
            self.defense = 3
            print("Te voilà équipé d'un bouclier pendant 3 tours !")
        # Retour sur combat
        return self.defense
        
        
        
    def drink_potion(self):
        """This function gives back 20 HP to the player in battle."""
        if self.hp < self.hp_max -20:
            self.hp += 20
        else:
            self.hp = self.hp_max
        self.potion -= 1
        print(f'-------Vous avez maintenant {self.potion} potions et {self.hp}PV')
        # Retour sur combat
        return self.hp, self.potion
               
