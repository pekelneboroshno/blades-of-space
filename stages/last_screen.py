import pygame
from blades_of_space.settings import WIDTH, HEIGHT
from pygame.sprite import GroupSingle, Group
from .stage_protocol import BaseStage


class LastScreen(BaseStage):

    def __init__(self, player: GroupSingle, engine):
        self.enemies = Group()
        super().__init__(player, engine)

        self.title = pygame.font.\
                SysFont('corbel', 40, True). \
                render('Thanks for playing!', True, (255, 255, 255))

    def run(self):

        self.engine.screen.blit(
            self.title, (WIDTH // 2 - self.title.get_width() // 2,
            HEIGHT // 2)
        )
        super().run()
