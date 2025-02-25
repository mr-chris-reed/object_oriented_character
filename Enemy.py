import pygame

class Enemy:

    def __init__(self, sprite_sheet_list, x, y, delta_x, delta_y, able_to_attack_distance, attack_power):
        self.sprite_sheet_list = sprite_sheet_list
        self.x = x
        self.y = y
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.able_to_attack_distance = able_to_attack_distance
        self.attack_power = attack_power
        self.touch_time_threshold = 2
        self.touch_time = 0

        self.sprite = pygame.image.load(self.sprite_sheet_list).convert_alpha()
        self.sprite_scale_factor = 0.2
        self.sprite_width = self.sprite.get_rect().width * self.sprite_scale_factor
        self.sprite_height = self.sprite.get_rect().height * self.sprite_scale_factor
        self.sprite = pygame.transform.scale(self.sprite, (self.sprite_width, self.sprite_height))

    def moveTowardsPlayer(self, player):
        if self.x > player.x:
            self.x -= self.delta_x
        elif self.x < player.x:
            self.x += self.delta_x
        if self.y > player.y:
            self.y -= self.delta_y
        elif self.y < player.y:
            self.y += self.delta_y

    def canAttack(self, player):
        if abs(self.x - player.x) <= self.able_to_attack_distance and abs(self.y - player.y) <= self.able_to_attack_distance:
            return True
        else:
            return False

    def attack(self, player):
        enemy_rect = self.sprite.get_rect()
        player_rect = player.get_sprite().get_rect()
        if (enemy_rect.colliderect(player_rect)):
            self.touch_time += 1
        if (self.touch_time >= self.touch_time_threshold):
            player.health -= self.attack_power
            self.touch_time = 0
            #print(player.health)