import pygame
import random
from dataclasses import dataclass, field
from typing import Union
from pygame import Rect


YELLOW = (255, 255, 0)
BLOODY_RED = (153, 0, 51)
LIGHT_YELLOW = (153, 255, 204)


def generate_direction() -> tuple:
    return random.uniform(-2, 2) , random.uniform(-2, 2)


@dataclass
class Spark:
    x: int
    y: int
    width: int = field(default_factory=lambda: random.randint(5, 7))
    height: int = field(default_factory=lambda: random.randint(2, 7))
    color: tuple = field(default_factory=lambda: random.choice([YELLOW, BLOODY_RED, LIGHT_YELLOW]))
    vel: float = field(default_factory=lambda: random.uniform(0.1, 1.5))
    timer: int = field(default_factory=lambda: random.randint(-25, 0))
    is_visible: bool = True
    rect: Rect | None = None
    direction: tuple = field(default_factory=generate_direction)

    def draw(self, win):
        if self.timer < 100:
            self.rect = pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height))

        self.timer += 1
        self.x += self.direction[0] * self.vel
        self.y += self.direction[1] * self.vel


class Explosion:
    sparks: list[Spark] = field(default_factory=list)

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.sparks = [Spark(self.x, self.y) for i in range(200)]

    def draw(self, win):
        for spark in self.sparks:
            spark.draw(win)
