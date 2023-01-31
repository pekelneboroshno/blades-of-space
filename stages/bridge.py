import pygame

from .stage_protocol import BaseStage
from pygame.sprite import GroupSingle
from blades_of_space.settings import STAGE_FINISHED


class BridgeStage(BaseStage):

    def __init__(self, player: GroupSingle, engine):
        super().__init__(player, engine)
        self.enemies = pygame.sprite.Group()

    def run(self):
        super().run()
