import pygame
from typing import Generator
from pygame.sprite import Group, GroupSingle
from ..enemies import Bee
from ..player import lazers, Lazer
from ..explosion import Explosion
from ..background import Background
from ..settings import HEIGHT, STAGE_FINISHED
from ..event_handlers import setup_shoot_event_handler


class Stage:

    def __init__(self, player: GroupSingle, enemies: Group, screen):
        self.player = player
        self.enemies = enemies
        self.screen = screen
        self.explosions: list[Explosion] = []
        self.background = Background()
        self.init_sound()
        self.reset_direction: Generator = self.reset_appearence()

    def init_sound(self):
        setup_shoot_event_handler()

    def process_lazer_collision(self, enemies: pygame.sprite.Group, lazer: Lazer) -> bool:
        for enemy in enemies:
            if pygame.sprite.collide_rect(enemy, lazer):
                enemy.kill()
                return True
        return False

    def draw_explosions(self):
        for explosion in self.explosions:
            explosion.draw(self.screen)

    def reset_appearence(self):
        while True:
            timeout = 0
            increase_timeout = 20
            for enemy in self.enemies:
                enemy.timeout = timeout
                enemy.ai = Bee.bee_ai_left
                enemy.rect.x, enemy.rect.y = Bee.LEFT_START_POSITION
                timeout += increase_timeout
            yield
            timeout = 0
            for enemy in self.enemies:
                enemy.timeout = timeout
                enemy.ai = Bee.bee_ai_right
                enemy.rect.x, enemy.rect.y = Bee.RIGHT_START_POSITION
                timeout += increase_timeout
            yield

    def is_enemies_visible(self):
        for i, enemy in enumerate(self.enemies):
            if i + 1 == len(self.enemies):
                if enemy.rect.y >= HEIGHT + 300:
                    next(self.reset_direction)

    def process_player_collisions(self):
        enemy = self.player.sprite & self.enemies
        if enemy:
            enemy.kill()
            self.explosions.append(Explosion(
                enemy.rect.x + enemy.rect.width / 2,
                enemy.rect.y + enemy.rect.height / 2
            ))

    def run(self):
        self.background.custom_update(self.screen, HEIGHT)

        self.player.draw(self.screen)
        self.player.update()

        self.enemies.draw(self.screen)
        self.enemies.update()

        self.is_enemies_visible()

        lazers.draw(self.screen)
        lazers.update()

        for lazer in lazers:
            hit = self.process_lazer_collision(self.enemies, lazer)
            if hit:
                lazer.kill()
                self.explosions.append(Explosion(lazer.rect.x, lazer.rect.y))

        self.process_player_collisions()

        self.draw_explosions()
        if not len(self.enemies):
            return STAGE_FINISHED
