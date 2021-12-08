from dataclasses import dataclass
from typing import ClassVar
from abc import ABCMeta, abstractmethod

@dataclass
class Entity(metaclass = ABCMeta):
    
    name : str
    hp : int
    hp_max : int
    attack : int

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

    def level(self,floor,difficulty):
        """ This function give the force and the health points of the monster, using the floor's level and the difficulty's level."""
        attack_base = 4
        hp_base = 20
        droprate_base = 10
        points_base = 10

        self.droprate = droprate_base * (((floor/10)+difficulty)+1)
        self.attack = round(attack_base * (((floor/10)+difficulty)+1))
        self.hp = round(hp_base * (((floor/10)+difficulty)+1))
        self.points = round(points_base * (((floor/10)+difficulty)+1))
        print(f"{self.name} vient d'apparaître ! Un monstre avec {self.hp} points de vie et avec une force de {self.attack}.")
        return self.points, self.droprate, self.attack, self.hp

    def attack(self,player):
        """This function takes away health points from life's player when an ennemy attacks him."""
        if player.defense != 0 :
            self.weak_attack = round(self.attack / 1.5)
            player.defense -= 1
            player.hp -= self.weak_attack
            print(f"Vous avez subi {self.weak_attack} points de dégâts de la part du {self.name}")

        else:    
            player.hp -= self.attack
            print(f"Vous avez subi {self.attack} points de dégâts de la part du {self.name}")
            print(f'Il vous reste {player.hp} points de vie.')
            # Come back to the fight
            return player.hp


    def death(self,player,drop):
        """"This function will delete the last summoned monster and run the drop() method"""

        print("Félicitations ! Vous avez réussi à vaincre {self.name}!")
        del self
        drop.drop()
        # Come back to the fight 
        return 0

class Boss(Entity):

    points : ClassVar[int]
    droprate : ClassVar[float]
    weak_attack : ClassVar[float]
    defense : ClassVar[int]

    def level(self,floor,difficulty):
        """ This function give the force and the health points of the boss, using the floor's level and the difficulty's level."""
        attack_base = 6
        hp_base = 30
        droprate_base = 15
        points_base = 15

        self.droprate = droprate_base * (((floor/10)+difficulty)+1)
        self.attack = round(attack_base * (((floor/10)+difficulty)+1))
        self.hp = round(hp_base * (((floor/10)+difficulty)+1))
        self.points = round(points_base * (((floor/10)+difficulty)+1))
        print(f"{self.name} vient d'apparaître ! Un boss avec {self.hp} points de vie et avec une force de {self.attack}.")
        return self.points, self.droprate, self.attack, self.hp

    def attack(self,player):
        """This function takes away health points from life's player when the Boss attacks him."""
        if player.defense != 0 :
            self.weak_attack = round(self.attack / 1.5)
            player.defense -= 1
            player.hp -= self.weak_attack
            print(f"Vous avez subi {self.weak_attack} points de dégâts de la part du {self.name}")

        else:    
            player.hp -= self.attack
            print(f"Vous avez subi {self.attack} points de dégâts de la part du {self.name}")
            print(f'Il vous reste {player.hp} points de vie.')
            # Come back to the fight
            return player.hp

    def death(self,drop=None):
        """"This function will delete the last summoned monster and run the drop() method"""
        print("Félicitations ! Vous avez réussi à vaincre {self.name}!")
        del self
        # drop.drop()
        # Come back to the fight
    
    def defense(self):
        """This function give a protection to the Boss during 3 turns."""
        self.defense = 3
        print(f"{self.name} vient de s'équiper d'une protection pendant 3 tours !")
        # Come back to the fight
        return self.defense

@dataclass
class Player(Entity):
    
    def __post_init__(self):
        self.potion = 3
        self.defense = 0
        self.score = 0
        
    def attack(self,monster):
         """This function takes away health points from life's ennemy when the player attacks."""
         if monster.hp <= self.attack:
        
            monster.death()
            print("Félicitation,Vous avez réussi à vaincre l'ennemi!")
            # Retour sur combat 
            return 0
         else:
            print(f'Il reste {monster.hp - self.attack} PV à l\'ennemi')
            # Retour sur combat
            return monster.hp - self.attack
    
    def death(self):
        playing = False
        print(f"Vous êtes mort ! Votre score est de {self.score}")
        return playing, self.score
    
    def defense_player(self):
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
               
        
    def quit(self):
        playing = False
        print(f"Vous quiez le geux! Votre score est de {self.score}")
        return playing
