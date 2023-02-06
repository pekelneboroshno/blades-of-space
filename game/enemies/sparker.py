import pygame
import os

from game.settings import PROJECT_DIR, WIDTH
from game.weapons import VeryBigLazer

from .base import Enemy


class Right:

    direction = "right"

    def move(self) -> tuple:
        return (-1.5, 0)


class Left:

    direction = "left"

    def move(self) -> tuple:
        return (1.5, 0)


class Sparker(Enemy):

    left_movement = Left()
    right_movement = Right()


    def __init__(self, timeout = 0):
        self.timeout = timeout
        super().__init__(self.right_movement)
        self.velocity = 2
        self.rect.x, self.rect.y = WIDTH + self.rect.width, 50
        self.hp = 16
        self.lazers = pygame.sprite.Group()

    def update(self, screen):
        super().update()
        self.shoot()

        self.lazers.draw(screen)
        self.lazers.update()

    def shoot(self):
        if self.timeout % 75 == 0 or self.timeout % 72 == 0:
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
        self.timeout -= 1
        if self.timeout < 0:
            super().move()

        if self.rect.x < 0:
            self.movement = self.left_movement

        elif self.rect.x > WIDTH - self.rect.height + 40 and self.movement.direction == "left":
             self.movement = self.right_movement

    def set_image(self):
        self.image = pygame.transform.rotate(
            pygame.image.load(os.path.join(PROJECT_DIR, "images", "Sparker.png")).convert_alpha(), 180
        )
