import pygame
from .base import Enemy
from blades_of_space.settings import PROJECT_DIR, WIDTH


class Right:

    def move(self) -> tuple:
        return (-1.5, 1.5)


class Left:

    def move(self) -> tuple:
        return (1.5, 1.5)


class Ram(Enemy):

    bee_ai_left = Left()
    bee_ai_right = Right()

    RIGHT_START_POSITION = (WIDTH, -140)
    LEFT_START_POSITION = (-60, -140)

    def __init__(self, timeout = 0):
        self.timeout = timeout
        super().__init__(self.bee_ai_right)
        self.velocity = 1
        self.rect.x, self.rect.y = self.RIGHT_START_POSITION
        self.hp = 10

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