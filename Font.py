import pygame

class Font:

    def __init__(self, font_file, size, text):
        self.font_file = font_file
        self.size = size
        self.text = text

    def generate_text_surface(self):
        font = pygame.font.Font(self.font_file, self.size)
        text_surface = font.render(self.text, True, (255, 0, 0))
        return text_surface