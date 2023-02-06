import pygame
import os
from .base import Enemy
from game.settings import PROJECT_DIR, WIDTH


class Right:

    def move(self) -> tuple:
        return (-1.5, 1.5)


class Left:

    def move(self) -> tuple:
        return (1.5, 1.5)


class Bee(Enemy):

    left = Left()
    right = Right()

    RIGHT_START_POSITION = (WIDTH, -140)
    LEFT_START_POSITION = (-60, -140)

    def __init__(self, timeout = 0):
        self.timeout = timeout
        super().__init__(self.right)
        self.velocity = 4
        self.rect.x, self.rect.y = self.RIGHT_START_POSITION
        self.hp = 1

    def move(self):
        self.timeout -= 1
        if self.timeout < 0:
            super().move()

    def hit(self):
        self.hp -= 1
        if self.hp <= 0:
            self.kill()

    def set_image(self):
        self.image = pygame.transform.rotate(
            pygame.image.load(os.path.join(PROJECT_DIR, "images", "Bee.png")).convert_alpha(), 180
        )

    def update(self, screen):
        super().update()
