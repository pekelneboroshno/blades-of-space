from abc import ABC
from pygame.sprite import GroupSingle, Group
from typing import Any


class BaseStage(ABC):

    player: GroupSingle
    enemies: Group
    engine: Any


    def __init__(self, player: GroupSingle, engine):
        self.player = player
        self.engine = engine

    def run(self):

        self.player.draw(self.engine.screen)
        self.player.update()

        self.enemies.draw(self.engine.screen)
        self.enemies.update(self.engine.screen)

        self.engine.process_lazer_collision(self.enemies)
        self.engine.process_player_collisions(self.enemies)

        self.engine.draw_explosions()
