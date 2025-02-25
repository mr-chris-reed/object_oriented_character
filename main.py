import pygame, sys
from Background import Background
from Wraith import Wraith
from Hud import Hud
from Font import Font
from Enemy import Enemy
from StartScreen import StartScreen
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
pygame.font.init()
CANVAS = pygame.display.set_mode((W, H))
pygame.display.set_caption("WRAITH!")

backgrounds.append(Background("background_2.png", 0, 0, 100, 900, 100, 900))

clock = pygame.time.Clock()

total_seconds = 0

running = True

wraith = Wraith("wraith_V2.png", 10, W // 2, H // 2, 10, 10)

boss = Enemy("RPG_Boss_Sprite.png", 400, 400, 1, 1, 20, 2)

hud = Hud(wraith, backgrounds[0], clock)

start_screen = StartScreen("start_screen_background.png", W, H, 0, 0)

while running:

    total_seconds += clock.get_time() / 1000
    total_minutes = total_seconds // 60
    left_over_seconds = total_seconds % 60

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

    hud_line_1 = Font("Creepster-Regular.ttf", 45, hud.get_hud()[0])
    hud_line_2 = Font("Creepster-Regular.ttf", 45, hud.get_hud()[1])
    hud_line_3 = Font("Creepster-Regular.ttf", 45, f"{total_minutes:.0f}" + ":" + f"{left_over_seconds:.2f}")

    backgrounds[0].checkAndSetCharsPos(wraith)
    CANVAS.blit(start_screen.background, (start_screen.x, start_screen.y))
    # CANVAS.blit(backgrounds[0].get_background(), (backgrounds[0].get_x(), backgrounds[0].get_y()))
    CANVAS.blit(wraith.get_sprite(), (wraith.get_x(), wraith.get_y()))
    CANVAS.blit(boss.sprite, (boss.x, boss.y))
    CANVAS.blit(hud_line_1.generate_text_surface(), (25, 25))
    CANVAS.blit(hud_line_2.generate_text_surface(), (25, 75))
    CANVAS.blit(hud_line_3.generate_text_surface(), (25, 125))
    pygame.display.update()
    wraith.increment_counter()
    boss.moveTowardsPlayer(wraith)
    if (boss.canAttack(wraith)):
        boss.attack(wraith)
    clock.tick(FPS)

pygame.quit()
sys.exit()