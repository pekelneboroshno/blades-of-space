import pygame
from .stage_protocol import BaseStage
from typing import Generator
from pygame.sprite import GroupSingle
from blades_of_space.enemies import Bee
from blades_of_space.player import lazers
from blades_of_space.settings import HEIGHT, STAGE_FINISHED


class Stage(BaseStage):

    def __init__(self, player: GroupSingle, engine):
        super().__init__(player, engine)

        self.enemies = pygame.sprite.Group()
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
                enemy.timeout = timeout
                enemy.ai = Bee.bee_ai_left
                enemy.rect.x, enemy.rect.y = Bee.LEFT_START_POSITION
                timeout += increase_timeout
            yield
            timeout = 0
            for enemy in self.enemies:
                enemy.timeout = timeout
                enemy.ai = Bee.bee_ai_right
                enemy.rect.x, enemy.rect.y = Bee.RIGHT_START_POSITION
                timeout += increase_timeout
            yield

    def is_enemies_visible(self):
        for i, enemy in enumerate(self.enemies):
            if i + 1 == len(self.enemies):
                if enemy.rect.y >= HEIGHT + 300:
                    next(self.reset_direction)

    def run(self):
        super().run()

        self.is_enemies_visible()

        lazers.draw(self.engine.screen)
        lazers.update()

        if not len(self.enemies):
            return STAGE_FINISHED
