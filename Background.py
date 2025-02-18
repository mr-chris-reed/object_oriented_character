# background class
import pygame

class Background:

    def __init__(self, background, x, y):
        self.background = pygame.image.load(background).convert_alpha()
        self.x = x
        self.y = y

    def get_background(self):
        return self.background

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

