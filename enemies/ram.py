import pygame
from typing import Generator
from enum import Enum, auto
from .base import Enemy
from blades_of_space.settings import PROJECT_DIR, WIDTH, HEIGHT


class SkipStep(Enum):
    zero = auto()
    first = auto()
    second = auto()
    third = auto()
    fourth = auto()


def move() -> Generator:
    while True:
        yield (1.5, 0.0), SkipStep.zero
        yield (0.0, 4.0), SkipStep.first
        yield (0.0, -4.0), SkipStep.second


def move_left() -> Generator:
    while True:
        yield (-1.5, 0.0), SkipStep.zero
        yield (0.0, 4.0), SkipStep.first
        yield (0.0, -4.0), SkipStep.second


class Movement:

    def __init__(self, obj: Enemy):
        self.enemy = obj
        self.mv = move()
        self.skip_steps = set()
        direction, skip = next(self.mv)
        self.direction = direction
        self.skip_steps.add(skip)

    def allow_attack(self):
        return self.enemy.rect.x in range(100, WIDTH, 200) \
            and SkipStep.first not in self.skip_steps

    def allow_back(self):
        return self.enemy.rect.y in range(HEIGHT - self.enemy.rect.height, HEIGHT) \
            and SkipStep.second not in self.skip_steps

    def allow_right(self):
        return self.enemy.rect.x in range(100, WIDTH, 200) \
            and self.enemy.rect.y in range(25, 27) \
            and self.skip_steps == {SkipStep.zero, SkipStep.first, SkipStep.second}

    def allow_left(self):
        visible_enemy_from_right = WIDTH - self.enemy.rect.width
        return self.enemy.rect.x in range(visible_enemy_from_right - 10, visible_enemy_from_right) \
            and self.enemy.rect.y in range(25, 30)

    def allow_initial(self):
        return self.enemy.rect.x in range(0, 10) \
            and self.enemy.rect.y in range(25, 30) \

    def next_direction(self):
        direction, skip = next(self.mv)
        self.direction = direction
        self.skip_steps.add(skip)

    def reset_direction(self):
        self.skip_steps.clear()
        self.next_direction()

    def reset_left_direction(self):
        self.skip_steps.clear()
        self.mv = move_left()
        self.next_direction()
        self.moving_left = True

    def change_direction(self):
        if self.allow_attack():
            self.next_direction()
        elif self.allow_back():
            self.next_direction()
        elif self.allow_right():
            self.reset_direction()
        elif self.allow_left():
            self.reset_left_direction()
        elif self.allow_initial():
            self.reset_direction()

    def move(self) -> tuple[float, float]:
        self.change_direction()
        return self.direction


class Ram(Enemy):

    def __init__(self, timeout = 0):
        self.timeout = timeout
        super().__init__(Movement(self))
        self.velocity = 1
        self.rect.x, self.rect.y = -self.rect.width, 25
        self.hp = 20

    def move(self):
        self.timeout -= 1
        if self.timeout < 0:
            super().move()

    def update(self, screen):
        super().update()

    def set_image(self):
        self.image = pygame.transform.rotate(
            pygame.image.load(f"{PROJECT_DIR}/images/Ram.png" ).convert_alpha(), 0
        )

    def hit(self):
        self.hp -= 1
        if self.hp <= 0:
            self.kill()
