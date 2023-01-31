import pygame
from typing import Protocol
from blades_of_space.settings import WIDTH
from abc import ABCMeta, abstractmethod


class Movement(Protocol):
    def move(self) -> tuple:
        ...


class Enemy(pygame.sprite.Sprite, metaclass=ABCMeta):

    @abstractmethod
    def set_image(self):
        pass

    def __init__(self, movement: Movement, screen_x: int = WIDTH, screen_y: int = 0):
        self.image: pygame.Surface
        self.set_image()
        self.rect : pygame.Rect = self.image.get_rect(midbottom = (screen_x, screen_y))
        self.movement = movement
        self.velocity = 2
        super().__init__()

    def move(self):
        x, y = self.movement.move()
        self.rect.x += x * self.velocity
        self.rect.y += y * self.velocity

    def update(self):
        self.move()
