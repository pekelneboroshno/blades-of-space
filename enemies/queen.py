import pygame
import os

from .base import Enemy
from ..weapons import VeryBigLazer

from blades_of_space.settings import PROJECT_DIR, WIDTH, HEIGHT


class Static:

    def move(self) -> tuple:
        return (0, 0)


class MoveToPlace:

    def move(self) -> tuple:
        return (0, 3)


class Queen(Enemy):


    def __init__(self, timeout = 0):

        self.timeout = timeout
        super().__init__(MoveToPlace())
        self.velocity = 2
        self.hp = 30
        self.lazers = pygame.sprite.Group()

        self.rect.x, self.rect.y = (WIDTH // 2 - self.rect.height // 3, -100)
        self.arrived = False

    def update(self, screen):
        super().update()
        self.shoot()

        self.lazers.draw(screen)
        self.lazers.update()
        self.timeout += 1

    def shoot(self):
        if self.timeout % 100 == 0:
            self.lazers.add(
                VeryBigLazer(
                    self.rect.width // 2 + self.rect.x,
                    self.rect.height + self.rect.y
                )
            )

    def hit(self):
        self.hp -= 1
        if self.hp <= 0:
            self.kill()

    def move(self):
        super().move()
        if abs(self.rect.y) * 2.5 >= HEIGHT // 3 and not self.arrived:
            self.arrived = True
            self.movement = Static()

    def set_image(self):
        self.image = pygame.transform.rotate(
            pygame.image.load(os.path.join(PROJECT_DIR, "images", "Queen.png")).convert_alpha(), 180
        )
        self.image = pygame.transform.rotozoom(self.image, 1.0, 1.2)
