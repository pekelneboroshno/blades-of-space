import pygame
from typing import Self

from .stage_protocol import BaseStage
from pygame.sprite import GroupSingle
from blades_of_space.settings import STAGE_FINISHED
from blades_of_space.player import lazers


class BridgeStage(BaseStage):
    instance: Self | None = None

    def __init__(self, player: GroupSingle, engine):
        super().__init__(player, engine)
        self.enemies = pygame.sprite.Group()
        self.timer = 0

    def __new__(cls, *args, **kwargs):
        # Singleton!
        if not cls.instance:
            self = super().__new__(cls)
            cls.instance = self
            return self
        return cls.instance

    def reset_timer(self):
        self.timer = 0

    def run(self):

        lazers.draw(self.engine.screen)
        lazers.update()

        if self.timer <= 300:
            super().run()
            self.timer += 1
        else:
            return STAGE_FINISHED
