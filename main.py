import pygame, sys
import Wraith
from pygame.locals import *

# canvas variables
W = 1920
H = 1080

# frame rate
FPS = 60

# background color
BACKGROUND_COLOR = (255, 255, 255)

pygame.init()
CANVAS = pygame.display.set_mode((W, H))
pygame.display.set_caption("WRAITH!")

clock = pygame.time.Clock()

running = True

wraith = Wraith.Wraith("wraith_V2.png", 10, 0, 0, 10, 10)

while running:

    CANVAS.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        wraith.move_up()
    if keys[pygame.K_s]:
        wraith.move_down()
    if keys[pygame.K_a]:
        wraith.move_left()
    if keys[pygame.K_d]:
        wraith.move_right()

    CANVAS.blit(wraith.get_sprite(), (wraith.get_x(), wraith.get_y()))
    wraith.sprite_picker()
    pygame.display.update()
    wraith.increment_counter()
    clock.tick(FPS)

pygame.quit()
sys.exit()