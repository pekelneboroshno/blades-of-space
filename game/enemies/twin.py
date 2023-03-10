import pygame
import os
from game.settings import PROJECT_DIR, WIDTH
from game.weapons import BigLazer

from .base import Enemy


class Right:

    def move(self) -> tuple:
        return (-1, 0.7)


class Left:

    def move(self) -> tuple:
        return (1, 0.7)


class Circling:

    def __init__(self):
        def inner():
            while True:
                yield (0.5, 0)
                yield (0, 0.5)
                yield (-0.5, 0)
                yield (0, -0.5)

        self._inner_move = inner()
        self.timer = 0
        self.current_move = (0, 0)

    def move(self):
        self.timer += 1
        if self.timer % 15 == 0:
            self.current_move = next(self._inner_move)
        return self.current_move


SCREEN_MIDDLE = WIDTH / 2


class Twin(Enemy):

    left = Left()
    right = Right()
    circling = Circling()

    RIGHT_START_POSITION = (WIDTH, 0)
    LEFT_START_POSITION = (-230, 0)


    def __init__(self, timeout = 0, position: tuple = RIGHT_START_POSITION, config = right):
        self.timeout = timeout
        super().__init__(config)
        self.velocity = 2
        self.rect.x, self.rect.y = position
        self.hp = 10
        self.lazers = pygame.sprite.Group()

    def hit(self):
        self.hp -= 1
        if self.hp <= 0:
            self.kill()

    def shoot(self):
        if self.timeout % 55 == 0:
            self.lazers.add(
                BigLazer(
                    self.rect.width // 2 + self.rect.x,
                    self.rect.height + self.rect.y
                )
            )

    def move(self):
        self.timeout -= 1
        if self.timeout < 0:
            super().move()

        if (SCREEN_MIDDLE - 250 <= self.rect.x <= SCREEN_MIDDLE + 30) and not isinstance(self.movement, Circling):
            self.movement = self.circling

    def set_image(self):
        self.image = pygame.transform.rotate(
            pygame.image.load(os.path.join(PROJECT_DIR, "images", "Twin.png")).convert_alpha(), 180
        )
        self.image = pygame.transform.rotozoom(self.image, 1.0, 1.3)

    def update(self, screen):
        super().update()
        self.shoot()

        self.lazers.draw(screen)
        self.lazers.update()
