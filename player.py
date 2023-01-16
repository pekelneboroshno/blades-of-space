import pygame
from .settings import PROJECT_DIR
from .events import post_event


YELLOW = (255, 255, 0)


class Lazer(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((3, 10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()


lazers = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load(PROJECT_DIR + 'player.png').convert_alpha()
        self.rect : pygame.Rect = self.image.get_rect(midbottom = (400, 700))
        self.speed = 3
        self.fire_delay = 0
        self.screen = screen

    # player intersects with group
    def __and__(self, enemies: pygame.sprite.Group):

        for enemy in enemies:
            if pygame.sprite.collide_rect(enemy, self):
                return enemy

        return None

    @property
    def left_gun_pos(self):
        return self.rect.x + 41

    @property
    def right_gun_pos(self):
        return self.rect.x + 80

    def player_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

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
        return self.player_fire()
