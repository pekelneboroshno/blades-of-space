import pygame

from typing import Generator
from event_handlers import setup_shoot_event_handler
from pygame.sprite import GroupSingle
from background import Background
from explosion import Explosion
from stages import get_game_stage, BaseStage
from blades_of_space.player import lazers

from blades_of_space.settings import PROJECT_DIR

from .settings import WIDTH, HEIGHT



class TitleScreen:
    def __init__(self, screen):

        self.screen = screen

        self.image = pygame.image.load(PROJECT_DIR +  '/images/' + 'title_screen.jpg').convert()
        self.image = pygame.transform.smoothscale(self.image,(WIDTH, HEIGHT))

        font = pygame.font.SysFont('corbel', 68, True)
        self.text = font.render('Blades of Space', True, (255, 255, 255))

    def run(self):
        self.screen.blit(self.image,(0, 0))
        self.screen.blit(self.text, (20, 20))


class GameContext:
    """For running stages strategies"""


class EngineContext:

    def __init__(self, player: GroupSingle, screen):
        self.player = player
        self.background = Background()
        self.explosions: list[Explosion] = []
        self.screen = screen
        self.stages: Generator = get_game_stage(self.player, self)
        self.init_first_stage()
        self.init_sound()

    def next_stage(self):
        try:
            self.current_stage: BaseStage = next(self.stages)
        except StopIteration:
            print("game finished!")
            pygame.quit()
            exit()

        self.current_stage.engine = self

    init_first_stage = next_stage

    def init_sound(self):
        setup_shoot_event_handler()

    def draw_explosions(self):
        for explosion in self.explosions:
            explosion.draw(self.screen)

    def process_player_collisions(self, enemies):
        enemy = self.player.sprite & enemies
        if enemy:
            enemy.kill()
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
        self.background.custom_update(self.screen, HEIGHT)
        finished = self.current_stage.run()
        if finished:
            self.next_stage()
