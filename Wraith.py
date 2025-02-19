# wraith class
import pygame

class Wraith:

    def __init__(self, sprite_sheet, ts, x, y, x_delta, y_delta):
        self.sprite_sheet_width = None
        self.sprite_sheet_height = None
        self.sprite_scale_factor = None
        self.sprite_width = None
        self.sprite_height = None
        self.sprites = [] #
        self.sprites_left = [] #
        self.sprites_right = [] #
        self.sprite_index = 0
        self.counter = 0

        self.sprite_sheet = sprite_sheet
        self.ts = ts
        self.x = x
        self.y = y
        self.x_delta = x_delta
        self.y_delta = y_delta

        self.sprite_sheet = pygame.image.load(self.sprite_sheet).convert_alpha()
        self.sprite_sheet_width = self.sprite_sheet.get_rect().width
        self.sprite_sheet_height = self.sprite_sheet.get_rect().height
        self.sprite_scale_factor = 1.2
        self.sprite_sheet_width = self.sprite_sheet_width * self.sprite_scale_factor
        self.sprite_sheet_height = self.sprite_sheet_height * self.sprite_scale_factor
        self.sprite_sheet = pygame.transform.scale(self.sprite_sheet, (self.sprite_sheet_width, self.sprite_sheet_height))
        self.sprite_sheet_width = self.sprite_sheet.get_rect().width
        self.sprite_sheet_height = self.sprite_sheet.get_rect().height
        self.sprite_width = self.sprite_sheet_width // self.ts
        self.sprite_height = self.sprite_sheet_height

        for i in range(self.ts):
            rect = pygame.Rect(i * self.sprite_width, 0, self.sprite_width, self.sprite_height)
            image = self.sprite_sheet.subsurface(rect)
            self.sprites.append(image)

    def increment_counter(self):
        self.counter += 1

    def sprite_picker(self):
        if self.counter % 20 == 0: # adjust the number to the right of the "%" symbol to increase/decrease animation speed
            if self.sprite_index == self.ts - 1:
                self.sprite_index = 0
            else:
                self.sprite_index += 1

    def sprite_picker_left(self):
        if self.counter % 5 == 0: # adjust the number to the right of the "%" symbol to increase/decrease animation speed
            if self.sprite_index >= 0 and self.sprite_index <= 4 or self.sprite_index == 9:
                self.sprite_index = 5
            else:
                self.sprite_index += 1

    def sprite_picker_right(self):
        if self.counter % 5 == 0: # adjust the number to the right of the "%" symbol to increase/decrease animation speed
            if self.sprite_index >= 4:
                self.sprite_index = 0
            else:
                self.sprite_index += 1

    def get_sprite(self):
        return self.sprites[self.sprite_index]

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def keep_on_playable_space(self, background):
        sprite_rect = pygame.Rect(self.x, self.y, self.x + self.sprite_width, self.y + self.sprite_height)
        sprite_rect.clamp_ip(background.movable_space_rect)
        print(sprite_rect.left)
        print(sprite_rect.top)
        #print("sprite_rect type = ", type(sprite_rect))
        #print("movable_space_rect type = ", type(background.movable_space_rect))

    def move_up(self):
        self.y -= self.y_delta

    def move_down(self):
        self.y += self.y_delta

    def move_left(self):
        self.x -= self.x_delta

    def move_right(self):
        self.x += self.y_delta

    def jump():
        pass

    def attack():
        pass

    def jump():
        pass