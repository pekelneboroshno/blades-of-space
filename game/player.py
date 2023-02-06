import pygame
import os

from game.settings import PROJECT_DIR, HEIGHT, WIDTH
from game.events import post_event
from game.weapons import Lazer
from game.enums import Color

lazers = pygame.sprite.Group()

health_item = pygame.Surface((10, 10))
health_item.fill(Color.yellow.value)


class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load(os.path.join(PROJECT_DIR, 'images', 'player.png')).convert_alpha()
        self.rect : pygame.Rect = self.image.get_rect(midbottom = (400, 700))
        self.speed = 3
        self.fire_delay = 0
        self.screen = screen
        self.hp = 10

    # player intersects with group
    def __and__(self, group: pygame.sprite.Group):

        for item in group:
            if pygame.sprite.collide_rect(item, self):
                return item

        return None

    @property
    def left_gun_pos(self):
        return self.rect.x + 41

    @property
    def right_gun_pos(self):
        return self.rect.x + 80

    def player_movement(self):
        keys = pygame.key.get_pressed()

        # Handle borders
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x > WIDTH - self.rect.width:
            self.rect.x = WIDTH - self.rect.width
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > HEIGHT - self.rect.width:
            self.rect.y = HEIGHT - self.rect.width

        else:
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.speed
            if keys[pygame.K_UP]:
                self.rect.y -= self.speed
            if keys[pygame.K_DOWN]:
                self.rect.y += self.speed


    def draw_health_bar(self):
        for i in range(0, self.hp):
            self.screen.blit(health_item,(5 + i * 15, HEIGHT - 20))

    def player_fire(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.fire_delay == 0 and len(lazers) < 6:
            self.fire_delay = 60
            lazers.add(Lazer(self.left_gun_pos, self.rect.y))
            lazers.add(Lazer(self.right_gun_pos, self.rect.y))
            post_event("shoot")

    def update(self):
        if self.fire_delay != 0:
            self.fire_delay -= 1
        self.player_movement()
        self.player_fire()
        self.draw_health_bar()
