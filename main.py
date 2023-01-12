import pygame
from typing import Generator

from .settings import WIDTH, HEIGHT
from .stages import get_game_stage


def run():

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Blades of spaces v.0.1')

    stage: Generator = get_game_stage(screen)
    current_stage = next(stage)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            screen.fill((0,0,0))

        if current_stage.run():
            current_stage = next(stage)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    run()
