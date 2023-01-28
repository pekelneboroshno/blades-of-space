import pygame
from .stage_protocol import BaseStage
from typing import Generator
from pygame.sprite import GroupSingle
from blades_of_space.enemies import Bee
from blades_of_space.player import lazers
from blades_of_space.explosion import Explosion
from blades_of_space.settings import HEIGHT, STAGE_FINISHED


class Stage(BaseStage):

    def __init__(self, player: GroupSingle, engine):
        self.player = player
        self.enemies = pygame.sprite.Group()
        for timeout in range(0, 200, 20):
            self.enemies.add(
                Bee(timeout),
            )

        self.reset_direction: Generator = self.reset_appearence()
        self.engine = engine

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

        self.player.draw(self.engine.screen)
        self.player.update()

        self.enemies.draw(self.engine.screen)
        self.enemies.update()

        self.is_enemies_visible()

        lazers.draw(self.engine.screen)
        lazers.update()

        for lazer in lazers:
            hit = self.engine.process_lazer_collision(self.enemies, lazer)
            if hit:
                lazer.kill()
                self.engine.explosions.append(Explosion(lazer.rect.x, lazer.rect.y))

        self.engine.process_player_collisions(self.enemies)

        self.engine.draw_explosions()
        if not len(self.enemies):
            return STAGE_FINISHED
