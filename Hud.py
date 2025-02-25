import pygame

class Hud:

    def __init__(self, character, screen, clock):
        self.character = character
        self.screen = screen
        self.clock = clock
        self.time_since_start = 0

    def get_hud(self):
        self.time_since_start += pygame.time.get_ticks()
        seconds = self.time_since_start // 1000
        minutes = seconds // 60
        left_over_seconds = seconds % 60
        time_string = str(minutes) + ":" + f"{left_over_seconds:.2f}"
        hudArray = [
                    str(self.character.health), 
                    str(self.character.gold),
                    time_string,
                   ]
        return hudArray

