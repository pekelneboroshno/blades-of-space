import pygame
import random
from dataclasses import dataclass, field
from pygame import Rect
from blades_of_space.enums import Color


def generate_direction() -> tuple:
    return random.uniform(-2, 2) , random.uniform(-2, 2)


@dataclass
class Spark:
    x: int
    y: int
    width: int = field(default_factory=lambda: random.randint(5, 7))
    height: int = field(default_factory=lambda: random.randint(2, 7))
    color: tuple = field(default_factory=lambda: random.choice([
        Color.yellow.value, Color.bloody_red.value, Color.light_yellow.value
    ]))
    vel: float = field(default_factory=lambda: random.uniform(0.1, 1.5))
    timer: int = field(default_factory=lambda: random.randint(-25, 0))
    is_visible: bool = True
    rect: Rect | None = None
    direction: tuple = field(default_factory=generate_direction)

    def draw(self, screen):
        if self.timer < 100:
            self.rect = pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))

        self.timer += 1
        self.x += self.direction[0] * self.vel
        self.y += self.direction[1] * self.vel


class Explosion:
    sparks: list[Spark] = field(default_factory=list)

    def __init__(self, x: int, y: int, sparks_count: int = 200):
        self.x = x
        self.y = y
        self.sparks = [Spark(self.x, self.y) for _ in range(sparks_count)]

    def draw(self, screen):
        for spark in self.sparks:
            spark.draw(screen)
