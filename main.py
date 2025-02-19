import pygame, sys
import Background, Wraith
from pygame.locals import *

# canvas variables
W = 1106
H = 1021

# frame rate
FPS = 60

# background color
BACKGROUND_COLOR = (0, 0, 0)

backgrounds = []

pygame.init()
CANVAS = pygame.display.set_mode((W, H))
pygame.display.set_caption("WRAITH!")

backgrounds.append(Background.Background("background_2.png", 0, 0, 100, 900, 100, 900))

clock = pygame.time.Clock()

running = True

wraith = Wraith.Wraith("wraith_V2.png", 10, W // 2, H // 2, 10, 10)

while running:

    CANVAS.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
            wraith.move_up()
            wraith.sprite_picker_right()
    if keys[pygame.K_s]:
            wraith.move_down()
            wraith.sprite_picker_left()
    if keys[pygame.K_a]:
            wraith.move_left()
            wraith.sprite_picker_left()
    if keys[pygame.K_d]:
            wraith.move_right()
            wraith.sprite_picker_right()

    CANVAS.blit(backgrounds[0].get_background(), (backgrounds[0].get_x(), backgrounds[0].get_y()))
    CANVAS.blit(wraith.get_sprite(), (wraith.get_x(), wraith.get_y()))
    wraith.keep_on_playable_space(backgrounds[0])
    pygame.display.update()
    wraith.increment_counter()
    clock.tick(FPS)

pygame.quit()
sys.exit()