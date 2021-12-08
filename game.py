from entity import Player, Boss, Monster
from drop import Drop

class Game:
    def __init__(self):
        self.running = True
        self.introducing()

    def introducing(self):
        print("Bienvenue sur le jeu : 'Simplon Escape' !")
        print("Le but du jeu est de sauver la princesse Claire emprisonnée en haut du donjon Simplon.co. \nVous êtes le Héros de cette quête et partez à la rescousse de la princesse. \nVous aurez à affronter de nombreux ennemis au cours de votre ascension dans le donjon.")
        defi = input("-----------\nEtes-vous prêt(e) à relever ce défi ? (Y/N) ")
        while not self.running:
            if defi.lower() == "y":
                self.running = True
                self.run()
            elif defi.lower() == "n":
                print("Votre décision est lourde de conséquences. Claire restera dans son donjon pour le restant de ses jours...\n Ouste péant ! Reviens quand tu seras un peu plus valeureux !")
                break
            else:
                defi = input("Toi pas comprendre ? Y or N ? ")

    def run(self):
        while self.running:
            pass

        