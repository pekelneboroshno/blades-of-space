import pygame
from typing import Generator
from blades_of_space.player import Lazer
from event_handlers import setup_shoot_event_handler
from pygame.sprite import GroupSingle
from background import Background
from explosion import Explosion
from stages import get_game_stage, BaseStage
from blades_of_space.settings import HEIGHT


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

    def process_lazer_collision(self, enemies: pygame.sprite.Group, lazer: Lazer) -> bool:
        for enemy in enemies:
            if pygame.sprite.collide_rect(enemy, lazer):
                enemy.hit()
                return True
        return False

    def run(self):
        self.background.custom_update(self.screen, HEIGHT)
        finished = self.current_stage.run()
        if finished:
            self.next_stage()