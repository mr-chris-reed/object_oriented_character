import pygame

class StartScreen:

    def __init__(self, background, width, height, x, y):
        self.background = pygame.image.load(background).convert_alpha()
        self.width = width
        self.height = height
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.x = x
        self.y = y
        self.title = "Wraith Wars"
