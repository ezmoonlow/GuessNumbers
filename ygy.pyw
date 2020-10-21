import pygame
import random

Login = "IT-KvantumVL"
number = random.randint(0, 100)
W = 480
H = 360
SILVER = (0, 255, 255)
GOLD = (0, 255, 255)
BLACK = (0, 0, 0)
numeral = ""
move = 1
block = 0
start = 1
OUTSIDE_BG = (0, -100)


bg = pygame.image.load('Image/fonf.png')
bg_rect = bg.get_rect(topleft=(0, 0))

pygame.init()
pygame.display.set_caption('Угадай число')
screen = pygame.display.set_mode((W, H))
pygame.mouse.set_visible(False)

'''image = pygame.transform.scale(image.get_width() * 2, image.get_height() * 2)'''


font = pygame.font.SysFont('Arial', 28, True, False)
font_box = pygame.Surface((W - font.get_height(), font.get_height()))
font_rect = font_box.get_rect(center=(W // 2, H - font.get_height()))
font2 = pygame.font.SysFont('Arial', 14, False, True)

cat = pygame.image.load('Image/mars.png')
cat_rect = cat.get_rect(center=(70, 220))

dog = pygame.image.load('Image/erth.png')
dog_rect = cat.get_rect(center=(320, 170))

owl = pygame.image.load('Image/sun.png')
owl_rect = cat.get_rect(center=(210, 120))


dialog = pygame.image.load('Image/dialog.png')
dialog_rect = dialog.get_rect()
dialog_cat_pos = (cat_rect.x, cat_rect.y - dialog_rect.h)
dialog_dog_pos = (290, 70)
dialog_owl_pos = (owl_rect.x, owl_rect.y - dialog_rect.h)


def dialogs(text, pos, owl_text):
    screen.blit(dialog, pos)
    screen.blit(font2.render(text, True, BLACK), (pos[0] + 5, pos[1] + 5))
    screen.blit(dialog, dialog_owl_pos)
    screen.blit(font2.render(owl_text, True, BLACK), (dialog_owl_pos[0] + 5, dialog_owl_pos[1] + 5))
    pygame.display.update()
    pygame.time.wait(2000)


run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False
            elif e.unicode.isdecimal() and block == 0:
                numeral += e.unicode
            elif e.key == pygame.K_BACKSPACE:
                numeral = numeral[:-1]
            elif e.key == pygame.K_RETURN and numeral:
                if int(numeral) > 100:
                    dialogs('', OUTSIDE_BG, 'число 0-100')
                elif int(numeral) > number:
                    dialogs('', OUTSIDE_BG, 'Число меньше')
                elif int(numeral) < number:
                    dialogs('', OUTSIDE_BG, 'Число больше')
                if move == 1:
                    if int(numeral) == number:
                        dialogs(f'Это число {numeral}', dialog_cat_pos, 'Марс, ты выйграл')
                        block = 1
                    else:
                        dialogs('Земля, твой ход', dialog_cat_pos, 'Продолжаем')

                if move == 2:
                    if int(numeral) == number:
                        dialogs(f'Это число {numeral}', dialog_dog_pos, 'Земля, ты выйграла')
                        block = 1
                    else:
                        dialogs('Марс, твой ход', dialog_dog_pos, 'Продолжаем')
                numeral = ''
                move += 1
                if move > 2:
                    move = 1


    screen.blit(bg, bg_rect)
    screen.blit(cat, cat_rect)
    screen.blit(dog, dog_rect)
    screen.blit(owl, owl_rect)
    screen.blit(font_box, font_rect)
    font_box.fill(SILVER)
    font_box.blit(font.render(numeral, True, BLACK), (10, 0))
    pygame.display.update()

    if start == 1:
        dialogs('', OUTSIDE_BG, 'Я загадала число')
        dialogs('', OUTSIDE_BG, 'От 0 до 100')
        dialogs('Марс, твой ход', dialog_dog_pos, 'Отгадайте его')
        start = 0
