import pygame

from .stage_protocol import BaseStage
from pygame.sprite import GroupSingle
from blades_of_space.enemies import Sparker
from blades_of_space.player import lazers
from blades_of_space.settings import STAGE_FINISHED


class Stage4(BaseStage):

    def __init__(self, player: GroupSingle, engine):
        super().__init__(player, engine)

        self.enemies = pygame.sprite.Group()
        self.enemies.add(
            Sparker()
        )

    def run(self):
        super().run()

        if not len(self.enemies):
            return STAGE_FINISHED
