import pygame
from pathlib import Path

from game.player import Player

from game.settings import WIDTH, HEIGHT
from game.engine import EngineContext
from game.enums import Color


def run():

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Blades of spaces v.1.0.0')

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
    import sys
    sys.path.append(str(Path.cwd()))
    run()
