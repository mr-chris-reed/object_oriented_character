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

    def checkAndSetCharsPos(self, character):
        if (character.x <= self.low_x):
            character.x = self.low_x
        if (character.x >= self.high_x - character.sprite_width / 2):
            character.x = self.high_x - character.sprite_width / 2
        if (character.y <= self.low_y):
            character.y = self.low_y
        if (character.y >= self.high_y - character.sprite_height):
            character.y = self.high_y - character.sprite_height
