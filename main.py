import pygame

from .player import Player

from .settings import WIDTH, HEIGHT
from .engine import EngineContext
from .enums import Color


def run():

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Blades of spaces v.0.2.6')

    player = pygame.sprite.GroupSingle()
    player.add(Player(screen))

    engine = EngineContext(player, screen)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            screen.fill(Color.black.value)

        engine.run()

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    run()
