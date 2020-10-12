import pygame
import random

Login = "IT-KvantumVL"
number = random.randint(0, 100)
W = 580
H = 460
SILVER = (255, 250, 205)
GOLD = (209, 202, 59)

pygame.init()
pygame.display.set_caption('Угадай число')
screen = pygame.display.set_mode((W, H))
pygame.mouse.set_visible(False)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False