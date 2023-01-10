import pygame
from .stage1 import Stage
from ..enemies import Bee, BeeAI
from ..player import Player


def get_game_stage(screen):
    player = pygame.sprite.GroupSingle()
    player.add(Player())

    enemies = pygame.sprite.Group()
    for timeout in range(0, 200, 20):
        enemies.add(
            Bee(BeeAI(), timeout),
        )
    yield Stage(player=player, enemies=enemies, screen=screen)

    for timeout in range(0, 20, 20):
        enemies.add(
            Bee(BeeAI(), timeout),
        )

    yield Stage(player=player, enemies=enemies, screen=screen)
