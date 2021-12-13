from entity import Player, Boss, Monster
from random import randint
from termcolor import colored
import time
import os

clear = lambda: os.system('cls')

class Game:
    def __init__(self):
        self.running = True
        self.floor = 1
        self.score = 0
        self.introducing()

    def introducing(self):
        print(colored('Bienvenue sur le jeu :', 'white'),colored( 'Simplon Escape !', 'red'))
        print("Le but du jeu est de sauver la princesse" ,colored("Claire","red"), "emprisonnée en haut du donjon Simplon.co. \nVous êtes le Héros de cette quête et partez à la rescousse de la princesse. \nVous aurez à affronter de nombreux ennemis au cours de votre ascension dans le donjon.")
        defi = input("----------------------------------------------------------------\nEtes-vous prêt(e) à relever ce défi ? (Y/N) ")
        while self.running:
            if defi.lower() == "y":
                self.run()
            elif defi.lower() == "n":
                self.running = False
                print("Votre décision est lourde de conséquences. Claire restera dans son donjon pour le restant de ses jours...\n Ouste péant ! Reviens quand tu seras un peu plus valeureux !")
                break
            else:
                defi = input("Toi pas comprendre ? Y or N ?    ")

    def run(self):
        clear()
        print("Votre bravoure vous honore ! Et ce sacrifice quasi certain restera à jamais dans les livres d'histoire ...")
        name = input("Mais au fait, quel(le) est ton nom jeune aventurier(ère) ?    ")
        player = Player(name, 50, 50, 5)
        print(colored(f"{player.name}","blue")," dis-tu... Ca reviendra certainement un jour à la mode.")
        time.sleep(1)
        print("Trêve de bavardages ! Il est temps pour toi de te confronter au plus grand défi de ta vie...")
        time.sleep(1)
        print("------------------------------------------ Génération du donjon ---------------------------------------------")
        time.sleep(2)
        clear()
        while self.running:
            choice = self.choice(player)
            if not choice:
                break
        if self.score != 0:
            with open("Scores.txt", 'a') as scores:
                scores.write(f'{player.name} =====> score = {self.score} | floor = {self.floor}\n')
                
    def choice(self, player):
        print(f"                           Vous arrivez à l'étage {self.floor} et votre score est de {self.score}\n")
        time.sleep(1)
        path = ""
        print("3 chemins s'offrent à vous, choisissez l'un d'entre eux ou abandonner lâchement.")
        while path not in ["a", "b", "c", "d"]:
            print("a: route facile | b: route normale | c: route difficile | d: abandonner lâchement")
            path = input("Quel chemin choisissez vous entre a | b | c | d ?      ")
            time.sleep(1)
            if path.lower() == "a":
                clear()
                difficulty = 0
                self.summon_monster(difficulty, player)
                path = ""

            elif path.lower() == "b":
                clear()
                difficulty = 0.1
                self.summon_monster(difficulty, player)
                path = ""

            elif path.lower() == "c":
                clear()
                difficulty = 0.2
                self.summon_monster(difficulty, player)
                path = ""

            elif path.lower() == "d":
                self.quit()
            else:
                print("Toi pas comprendre ?")
            if player.hp <= 0:
                break

    def summon_monster(self, difficulty, player):
        if self.floor % 5 == 0:
            list_boss_name = ["Dracula", "Frankenstein", "BigTroll", "Lucifer"]
            boss_name = list_boss_name[randint(0,len(list_boss_name)-1)]
            monster = Boss(boss_name, 35, 35, 8)
        else:
            list_monster_name = ["Un gobelin", "Un troll", "Un orc", "Un zombie", "Un mimic", "Yanis: le voleur d'excalibur"]
            monster_name = list_monster_name[randint(0,len(list_monster_name)-1)]
            monster = Monster(monster_name, 20, 20, 4)
        monster.level(self.floor, difficulty)
        self.fight(player, monster)

    def fight(self, player, monster):
        while player.hp > 0 and monster.hp > 0:
            choice = input("1: Attaque | 2: Défendre | 3: Potion\n")
            if choice == "1":
                time.sleep(1)
                self.score, monster.hp = player.attack(monster,self.score)
            elif choice == "2":
                time.sleep(1)
                clear()
                player.defense = player.defend()
            elif choice == "3":
                if player.potion > 0 :
                    time.sleep(1)
                    player.hp, player.potion = player.drink_potion()
                else:
                    print("Vous n'avez plus de potions")
            
            if monster.hp > 0 and choice in ["1", "2"]:
                player.hp = monster.attack(player)
        if player.hp <= 0 :
            self.running = player.death()
        else:
            del monster
            self.floor += 1
            print(f"Votre score est de ",colored(f"{self.score}","red")," et vous passez à l'étage ",colored(f"{self.floor}","red"))
            
    def quit(self):
        self.running = False
        print(f"Vous quittez le donjon! Votre score est de {self.score} et votre étage de {self.floor}")
            