import pygame
from pygame.sprite import Group, GroupSingle
from ..player import Player, LASSERS, Laser
from ..enemies import Bee
from ..explosion import Explosion
from ..background import Background
from ..settings import HEIGHT


def process_collision(enemies: pygame.sprite.Group, lasser: Laser, win):
    for enemy in enemies:
        if pygame.sprite.collide_rect(enemy, lasser):
            enemy.kill()


def draw_explosions(explosions: list[Explosion], win):
    for explosion in explosions:
        explosion.draw(win)


class Stage:

    def __init__(self, player: GroupSingle, enemies: Group, screen):
        self.player = player
        self.enemies = enemies
        self.screen = screen
        self.explosions = []
        self.background = Background()

    def run(self):
        self.background.custom_update(self.screen, HEIGHT)

        self.player.draw(self.screen)
        self.player.update()

        self.enemies.draw(self.screen)
        self.enemies.update()

        for lasser in LASSERS:
            lasser.draw(self.screen)

            hit = process_collision(self.enemies, lasser, self.screen)
            if hit:
                self.explosions.append(Explosion(lasser.rect.x, lasser.rect.y))

        draw_explosions(self.explosions, self.screen)



def get_game_stage(screen):
    player = pygame.sprite.GroupSingle()
    player.add(Player())

    enemies = pygame.sprite.Group()
    enemies.add(Bee(), Bee(250), Bee(50))
    yield Stage(player=player, enemies=enemies, screen=screen)
