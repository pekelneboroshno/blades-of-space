import pygame
import random

from dataclasses import dataclass, field
from blades_of_space.settings import PROJECT_DIR
from blades_of_space.explosion import Spark


class Background:

    def __init__(self):
        self.height = 1536
        self.image = pygame.image.load(PROJECT_DIR + 'starfield.jpg').convert()
        self.screen_pos = 0

    def custom_update(self, screen, screen_height):
        screen.blit(self.image,(0, -screen_height + self.screen_pos))
        screen.blit(self.image,(0, -screen_height - self.height + self.screen_pos))

        if self.screen_pos == self.height:
            self.screen_pos = 0

        self.screen_pos += 4


@dataclass
class Star(Spark):
    width: int = field(default_factory=lambda: random.randint(5, 7))
    height: int = field(default_factory=lambda: random.randint(2, 7))
    direction: tuple = (0.0, -1.0)
    timer: int = field(default_factory=lambda: random.randint(-155, 0))

    def draw(self, win):
        # if self.timer < 100:
        self.rect = pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height))

        # self.timer += 1
        # self.x += self.direction[0] * self.vel
        # self.y += self.direction[1] * self.vel
        # print(self.x)
        # print(self.y)


class DynamicBackground:

    def __init__(self, screen):
        self.screen = screen
        self.stars = [Star(10, 25) for _ in range(2)]

    def draw(self, win):
        for spark in self.stars:
            spark.draw(win)
