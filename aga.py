import pygame
import random

Login = "IT-KvantumVL"
number = random.randint(0, 100)
W = 480
H = 360
SILVER = (255, 250, 205)
GOLD = (209, 202, 59)
numeral = ""
move = 1
block = 0
start = 1
OUTSIDE_BG = (0, -100)


bg = pygame.image.load('Image/room.png')
bg_rect = bg.get_rect(topleft=(0, 0))

pygame.init()
pygame.display.set_caption('Угадай число')
screen = pygame.display.set_mode((W, H))
pygame.mouse.set_visible(False)

font = pygame.font.SysFont('Arial', 28, True, False)
font_box = pygame.Surface((W - font.get_height(), font.get_height()))
font_rect = font_box.get_rect(center=(W // 2, H - font.get_height()))
font2 = pygame.font.SysFont('Arial', 14, False, True)

cat = pygame.image.load('Image/cat.png')
cat_rect = cat.get_rect(center=(70, 220))

dog = pygame.image.load('Image/dog.png')
dog_rect = cat.get_rect(center=(410, 220))

owl = pygame.image.load('Image/owl.png')
owl_rect = cat.get_rect(center=(210, 120))


dialog = pygame.image.load('Image/dialog.png')
dialog_rect = bg.get_rect()
dialog_cat_pos = (cat_rect.x, cat_rect.y - dialog_rect.h)
dialog_dog_pos = (dog_rect.x - dialog_rect.w // 2, dog_rect.y - dialog_rect.h)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False

    screen.blit(bg, bg_rect)
    screen.blit(cat, cat_rect)
    screen.blit(dog, dog_rect)
    screen.blit(owl, owl_rect)
    pygame.display.update()