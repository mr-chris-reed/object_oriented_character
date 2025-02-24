import pygame

class Hud:

    def __init__(self, character, screen, clock):
        self.character = character
        self.screen = screen
        self.clock = clock

    def get_hud(self):
        hudString = (
                    str(self.character.health) + str('\n') + 
                    str(self.character.gold) + str('\n') +
                    str(pygame.time.get_ticks())
        )
        return hudString

