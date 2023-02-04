import pygame
from random import randint
from typing import Generator
from .enums import Color


x_speed = float
y_speed = float


def direction() -> tuple[x_speed, y_speed]:
    return (0, -5)


def direction_from_enemy() -> Generator:
    """tuple[x_speed, y_speed]:"""
    while True:
        yield (randint(-1, 3), randint(2, 3))


def up_to_down() -> tuple[x_speed, y_speed]:
    """tuple[x_speed, y_speed]:"""
    return (0, 5)


gen = direction_from_enemy()


class Lazer(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((3, 10))
        self.image.fill(Color.yellow.value)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction()

    def update(self):
        plus_x, plus_y = self.direction
        self.rect.x += plus_x
        self.rect.y += plus_y
        if self.rect.y <= 0 or self.rect.x <= 0:
            self.kill()


class BigLazer(Lazer):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.direction = next(gen)
        self.image = pygame.Surface((10, 10))
        self.image.fill(Color.some_other_color.value)


class VeryBigLazer(Lazer):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.direction = up_to_down()
        self.image = pygame.Surface((10, 25))
        self.image.fill(Color.red.value)
