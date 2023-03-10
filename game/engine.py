import pygame
from pygame.sprite import GroupSingle
from typing import Generator

from game.event_handlers import setup_shoot_event_handler, setup_game_music
from game.background import DynamicBackground
from game.explosion import Explosion
from game.stages import get_game_stage, BaseStage
from game.player import lazers
from game.settings import HEIGHT


from .events import post_event


class GameContext:
    """For running stages strategies"""


class EngineContext:

    def __init__(self, player: GroupSingle, screen):
        self.player = player
        self.screen = screen
        self.background = DynamicBackground(self.screen)
        self.explosions: list[Explosion] = []
        self.stages: Generator = get_game_stage(self.player, self)
        self.next_stage()
        self.init_sound()
        self.play_game_music()
        self.player_damage = 0

        self.controls = pygame.font.\
                SysFont('corbel', 18, True). \
                render('Arrows to move, Space to fire', True, (255, 255, 255))

    def show_controls(self):
        self.screen.blit(self.controls, (0, HEIGHT - 20))

    def next_stage(self):
        try:
            self.current_stage: BaseStage = next(self.stages)
        except StopIteration:
            print("Game finished!")
            print("Thanks for playing!")
            pygame.quit()
            exit()

        self.current_stage.engine = self


    def play_game_music(self):
        post_event("music")

    def init_sound(self):
        setup_shoot_event_handler()
        setup_game_music()

    def draw_explosions(self):
        for explosion in self.explosions:
            explosion.draw(self.screen)

    def process_player_collisions(self, enemies):
        enemy = self.player.sprite & enemies
        if enemy:
            self.player_damage += 1
            if self.player_damage == 50:
                self.player.sprite.hp -= 1
                self.player_damage = 0
                self.explosions.append(Explosion(
                    enemy.rect.x + enemy.rect.width / 2,
                    enemy.rect.y + enemy.rect.height / 2
                ))

        self.process_player_collisions_with_lazers(enemies)

    def process_player_collisions_with_lazers(self, enemies):
        player = self.player.sprite
        for enemy in enemies:
            if hasattr(enemy, 'lazers'):
                if lazer := self.player.sprite & enemy.lazers:
                    player.hp -= 1
                    self.explosions.append(Explosion(
                        lazer.rect.x,
                        lazer.rect.y
                    ))
                    lazer.kill()

    def process_lazer_collision(self, enemies: pygame.sprite.Group):
        for lazer in lazers:
            for enemy in enemies:
                if pygame.sprite.collide_rect(enemy, lazer):
                    enemy.hit()
                    lazer.kill()
                    self.explosions.append(Explosion(lazer.rect.x, lazer.rect.y))

    def run(self):
        self.background.draw(self.screen)
        finished = self.current_stage.run()
        if finished:
            self.next_stage()
