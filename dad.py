import pygame
import random

Login = "IT-KvantumVL"
number = random.randint(0, 100)
W = 700
H = 564
SILVER = (255, 250, 205)
GOLD = (209, 202, 59)
numeral = ""
move = 1
block = 0
start = 1
OUTSIDE_BG = (0, -100)

bg = pygame.image.load('Image/fonf.png')
bg_rect = bg.get_rect(topleft=(0, 0))

pygame.init()
pygame.display.set_caption('Земля')
screen = pygame.display.set_mode((W, H))
pygame.mouse.set_visible(False)

erth = pygame.image.load('Image/Erth.png')
erth_rect = erth.get_rect(center=(350, 270))





run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False
    screen.blit(bg, bg_rect)          
    screen.blit(erth, erth_rect)
    pygame.display.update()