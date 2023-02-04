import pygame
from typing import Generator

from .stage1 import Stage
from pygame.sprite import GroupSingle
from blades_of_space.enemies import Queen, Bee


class Stage5(Stage):

    def __init__(self, player: GroupSingle, engine):
        super().__init__(player, engine)

        self.enemies = pygame.sprite.Group()
        self.enemies.add(
            Queen()
        )

        for timeout in range(0, 200, 20):
            self.enemies.add(
                Bee(timeout),
            )

        self.reset_direction: Generator = self.reset_appearence()


    def reset_appearence(self):
        while True:
            timeout = 0
            increase_timeout = 20
            for enemy in self.enemies:
                if isinstance(enemy, Bee):
                    enemy.timeout = timeout
                    enemy.movement = Bee.left
                    enemy.rect.x, enemy.rect.y = Bee.LEFT_START_POSITION
                    timeout += increase_timeout
            yield
            timeout = 0
            for enemy in self.enemies:
                if isinstance(enemy, Bee):
                    enemy.timeout = timeout
                    enemy.movement = Bee.right
                    enemy.rect.x, enemy.rect.y = Bee.RIGHT_START_POSITION
                    timeout += increase_timeout
            yield
