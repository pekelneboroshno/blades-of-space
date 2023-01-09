import pygame
from copy import copy
from pygame.sprite import Group, GroupSingle
from ..enemies import Bee, BeeAI, bee_ai_left
from ..player import Player, LASSERS, Laser
from ..explosion import Explosion
from ..background import Background
from ..settings import HEIGHT


class Stage:

    def __init__(self, player: GroupSingle, enemies: Group, screen):
        self.player = player
        self.enemies = enemies
        self.screen = screen
        self.explosions: list[Explosion] = []
        self.background = Background()

    def process_collision(self, enemies: pygame.sprite.Group, lasser: Laser) -> bool:
        for enemy in enemies:
            if pygame.sprite.collide_rect(enemy, lasser):
                enemy.kill()
                return True

        return False

    def draw_explosions(self):
        for explosion in self.explosions:
            explosion.draw(self.screen)

    def reset_appearence(self):
        timeout = 0
        for enemy in self.enemies:
            enemy.timeout = timeout
            enemy.ai = bee_ai_left
            enemy.rect.x = 0
            enemy.rect.y = 0
            timeout += 30

    def is_enemies_visible(self):
        for i, enemy in enumerate(self.enemies):
            if i + 1 == len(self.enemies) and enemy.rect.x <= -HEIGHT:
                self.reset_appearence()

    def run(self):
        self.background.custom_update(self.screen, HEIGHT)

        self.player.draw(self.screen)
        self.player.update()

        self.enemies.draw(self.screen)
        self.enemies.update()

        self.is_enemies_visible()

        for lasser in LASSERS:
            lasser.draw(self.screen)

            hit = self.process_collision(self.enemies, lasser)
            if hit:
                self.explosions.append(Explosion(lasser.rect.x, lasser.rect.y))

        self.draw_explosions()


def get_game_stage(screen):
    player = pygame.sprite.GroupSingle()
    player.add(Player())

    enemies = pygame.sprite.Group()
    enemies.add(
        Bee(BeeAI()),
        Bee(BeeAI(), timeout=30),
        Bee(BeeAI(), timeout=60),
        Bee(BeeAI(), timeout=90),
        Bee(BeeAI(), timeout=120),
        Bee(BeeAI(), timeout=150),
        Bee(BeeAI(), timeout=180),
    )
    yield Stage(player=player, enemies=enemies, screen=screen)
