import pygame
from enum import Enum, auto
from .base import Enemy
from blades_of_space.settings import PROJECT_DIR, WIDTH, HEIGHT


class Direction(Enum):
    left = auto()
    right = auto()
    attack = auto()
    back = auto()


class Movement:

    def __init__(self, obj: Enemy):
        self.direction = Direction.right
        self.enemy = obj

    def allow_attack(self):
        return self.direction not in (Direction.attack, Direction.back) and \
            self.enemy.rect.x in range(100, WIDTH, 200)

    def change_direction(self):
        if self.allow_attack():
            self.direction = Direction.attack
        elif self.direction != Direction.back and self.enemy.rect.y in range(HEIGHT - self.enemy.rect.height, HEIGHT):
            self.direction = Direction.back

    def move(self) -> tuple[float, float]:
        self.change_direction()
        if self.direction == Direction.right:
            return (1.5, 0.0)
        elif self.direction == Direction.attack:
            return (0.0, 4.0)
        elif self.direction == Direction.back:
            return (0.0, -4.0)


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
