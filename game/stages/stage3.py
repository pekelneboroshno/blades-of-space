import pygame
from pygame.sprite import GroupSingle

from game.enemies import Ram
from game.player import lazers
from game.settings import STAGE_FINISHED

from .stage_protocol import BaseStage


class Stage3(BaseStage):

    def __init__(self, player: GroupSingle, engine):
        super().__init__(player, engine)

        self.enemies = pygame.sprite.Group()
        self.enemies.add(
            Ram()
        )

    def run(self):
        super().run()

        if not len(self.enemies):
            return STAGE_FINISHED
