import pygame
from pygame.sprite import GroupSingle, Group
from blades_of_space.settings import (
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
                render('press space to start', True, (255, 255, 255))

        self.developer = pygame.font.\
                SysFont('corbel', 18, True). \
                render('Pekelne Boroshno ©', True, (255, 255, 255))

        self.counter = 0

    def run(self):
        self.counter += 1

        self.engine.screen.blit(self.image,(0, 0))
        self.engine.screen.blit(self.title, (20, 20))

        if self.counter % 60 in range(0, 30):
            self.engine.screen.blit(self.start_game, (24, 80))

        self.engine.screen.blit(self.developer, (WIDTH - 160, HEIGHT - 20))
        return self.handle_game_start()

    def handle_game_start(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            return True
        return False
