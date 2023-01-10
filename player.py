import pygame
from dataclasses import dataclass
from pygame import Rect
from .settings import PROJECT_DIR
# from .events import post_event

YELLOW = (255, 255, 0)


@dataclass
class Laser:
    x: int
    y: int
    width: int = 3
    height: int = 10
    color: tuple = YELLOW
    vel: int = 4
    is_visible: bool = True
    rect: Rect = None

    def draw(self, win):
        self.y -= self.vel
        self.rect = pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height))


LASSERS: list[Laser] = []


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(PROJECT_DIR + 'player.png').convert_alpha()
        self.rect : pygame.Rect = self.image.get_rect(midbottom = (400, 700))
        self.move_speed = 3

    @property
    def left_gun_pos(self):
        return self.rect.x + 41

    @property
    def right_gun_pos(self):
        return self.rect.x + 80

    def player_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.move_speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.move_speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.move_speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.move_speed

    def player_fire(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            LASSERS.append(Laser(self.left_gun_pos, self.rect.y))
            LASSERS.append(Laser(self.right_gun_pos, self.rect.y))
        # post_event("shoot")

    def update(self):
        self.player_movement()
        return self.player_fire()
