import pygame

from .settings import WIDTH, HEIGHT
from .stages import get_game_stage


def run():

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Blades of spaces v.0.1')

    stage_gen = get_game_stage(screen)
    stage = next(stage_gen)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill((0,0,0))

        if stage.run():
            stage = next(stage_gen)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    run()
