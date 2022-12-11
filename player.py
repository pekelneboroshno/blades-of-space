import pygame
from sys import exit


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('player.png').convert_alpha()
        self.rect : pygame.Rect = self.image.get_rect(midbottom = (400, 700))
        self.move_speed = 3

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.move_speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.move_speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.move_speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.move_speed

    def update(self):
        self.player_input()
