# background class
import pygame

class Background:

    def __init__(self, background, x, y, low_x, high_x, low_y, high_y):
        self.background = pygame.image.load(background).convert_alpha()
        self.low_x = low_x
        self.high_x = high_x
        self.low_y = low_y
        self.high_y = high_y
        self.x = x
        self.y = y
        self.movable_space_rect = pygame.Rect(self.low_x, self.low_y, self.high_x, self.high_y)

    def get_background(self):
        return self.background

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_low_x(self):
        return self.low_x

    def get_high_x(self):
        return self.high_x

    def get_low_y(self):
        return self.low_y

    def get_high_y(self):
        return self.high_y
