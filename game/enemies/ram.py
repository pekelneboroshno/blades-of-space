import os
import pygame
from typing import Generator
from enum import Enum, auto

from game.settings import PROJECT_DIR, WIDTH, HEIGHT

from .base import Enemy


class SkipStep(Enum):
    zero = auto()
    first = auto()
    second = auto()
    third = auto()
    fourth = auto()


def start_position() -> Generator:
    while True:
        yield 60
        yield WIDTH // 2


class Movement:

    def __init__(self, obj: Enemy):
        self.enemy = obj
        self.skip_steps = set()
        self.moving_left = False
        self.start_position = start_position()
        self.next_direction()

    def next_direction(self):
        self.direction = next(self.start_position)

    def move(self) -> tuple[float, float]:
        if abs(self.enemy.rect.y) > HEIGHT + self.enemy.rect.height :
            self.enemy.rect.x = next(self.start_position)
            self.enemy.rect.y = -self.enemy.rect.height
        return (0.0, 5.0)


class Ram(Enemy):

    def __init__(self, timeout = 0):
        self.timeout = timeout
        super().__init__(Movement(self))
        self.velocity = 1
        self.rect.x, self.rect.y = 60, -self.rect.height
        self.hp = 20

    def move(self):
        self.timeout -= 1
        if self.timeout < 0:
            super().move()

    def update(self, screen):
        super().update()

    def set_image(self):
        self.image = pygame.transform.rotate(
            pygame.image.load(os.path.join(PROJECT_DIR, "images", "Ram.png")).convert_alpha(), 0
        )

    def hit(self):
        self.hp -= 1
        if self.hp <= 0:
            self.kill()
