import pygame
import random
from dataclasses import dataclass, field

from game.settings import WIDTH, HEIGHT
from game.explosion import Spark

from game.enums import Color


@dataclass
class Star(Spark):
    x: int = field(default_factory=lambda: random.randint(5, WIDTH - 5))
    y: int = field(default_factory=lambda: random.randint(5, HEIGHT - 5))
    width: int = field(default_factory=lambda: random.randint(5, 7))
    height: int = field(default_factory=lambda: random.randint(2, 7))
    direction: tuple = (0.0, 5.0)
    timer: int = field(default_factory=lambda: random.randint(-155, 0))
    width: int = field(default_factory=lambda: random.randint(1, 3))
    height: int = field(default_factory=lambda: random.randint(1, 3))
    color: tuple = Color.white.value


    def draw(self, win):
        if abs(self.y) <= abs(HEIGHT):

            self.rect = pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height))
            self.timer += 1
            self.x += self.direction[0] * self.vel
            self.y += self.direction[1] * self.vel

        else:
            self.y = 0


class DynamicBackground:

    def __init__(self, screen):
        self.screen = screen
        self.stars = [Star() for _ in range(160)]

    def draw(self, win):
        win.fill(Color.space_blue.value)
        for spark in self.stars:
            spark.draw(win)
