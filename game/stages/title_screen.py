import pygame
from pygame.sprite import GroupSingle, Group

from game.settings import (
    PROJECT_DIR, HEIGHT, WIDTH
)
from .stage_protocol import BaseStage


class TitleScreen(BaseStage):

    def __init__(self, player: GroupSingle, engine):
        super().__init__(player, engine)

        self.image = pygame.image.load(PROJECT_DIR +  '/images/' + 'title_screen.jpg').convert()
        self.image = pygame.transform.smoothscale(self.image,(WIDTH, HEIGHT))

        self.title = pygame.font.\
                SysFont('corbel', 68, True).\
                render('Blades of Space', True, (255, 255, 255))

        self.start_game = pygame.font.\
                SysFont('corbel', 18, True). \
                render('press enter to start', True, (255, 255, 255))

        self.developer = pygame.font.\
                SysFont('corbel', 18, True). \
                render('Pekelne Boroshno ©', True, (255, 255, 255))

        self.controls = pygame.font.\
                SysFont('corbel', 10, True). \
                render('arrows to move, space for fire', True, (255, 255, 255))


        self.counter = 0

    def run(self):
        self.counter += 1

        self.engine.screen.blit(self.image,(0, 0))
        self.engine.screen.blit(self.title, (20, 20))

        if self.counter % 40 in range(0, 30):
            self.engine.screen.blit(self.start_game, (24, 80))
        self.engine.screen.blit(self.controls, (24, 100))

        self.engine.screen.blit(self.developer, (WIDTH - 160, HEIGHT - 20))
        return self.handle_game_start()

    def handle_game_start(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            return True
        return False
