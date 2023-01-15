import pygame
from .base import Enemy
from blades_of_space.settings import PROJECT_DIR, WIDTH


class BeeAI:

    def move(self) -> tuple:
        return (-1.5, 1.5)


class BeeAILeft:

    def move(self) -> tuple:
        return (1.5, 1.5)


class Tween(Enemy):

    bee_ai_left = BeeAILeft()
    bee_ai_right = BeeAI()

    RIGHT_START_POSITION = (WIDTH, -140)
    LEFT_START_POSITION = (-60, -140)

    def __init__(self, timeout = 0):
        self.timeout = timeout
        super().__init__(self.bee_ai_right)
        self.velocity = 4
        self.rect.x, self.rect.y = self.RIGHT_START_POSITION

    def move(self):
        self.timeout -= 1
        if self.timeout < 0:
            super().move()

    def set_image(self):
        self.image = pygame.transform.rotate(
            pygame.image.load(f"{PROJECT_DIR}/images/Tween.png" ).convert_alpha(), 180
        )
