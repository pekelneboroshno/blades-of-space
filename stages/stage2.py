import pygame
from .stage_protocol import BaseStage
from pygame.sprite import GroupSingle
from blades_of_space.enemies import Twin
from blades_of_space.player import lazers
from blades_of_space.settings import STAGE_FINISHED


class Stage2(BaseStage):

    def __init__(self, player: GroupSingle, engine):
        super().__init__(player, engine)

        self.enemies = pygame.sprite.Group()
        self.enemies.add(
            Twin(0),
            Twin(0, Twin.LEFT_START_POSITION, Twin.ai_left)
        )

    def run(self):
        super().run()

        lazers.draw(self.engine.screen)
        lazers.update()

        if not len(self.enemies):
            return STAGE_FINISHED
