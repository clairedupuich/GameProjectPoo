
import pygame

pygame.init()
(largeur, hauteur) = (300, 500)
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption('Votre première fenêtre pygame ')
pygame.display.update()
running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False