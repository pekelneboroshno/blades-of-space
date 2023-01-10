import pygame
from .base import Enemy
from blades_of_space.settings import PROJECT_DIR


class BeeAI:

    def move(self) -> tuple:
        return (-1.5, 1.5)


class BeeAILeft:

    def move(self) -> tuple:
        return (1.5, 1.5)


bee_ai_left = BeeAILeft()
bee_ai_right = BeeAI()


class Bee(Enemy):

    def __init__(self, ai: BeeAI, timeout = 0):
        self.timeout = timeout
        super().__init__(bee_ai_right)
        self.velocity = 4

    def move(self):
        self.timeout -= 1
        if self.timeout < 0:
            super().move()

    def set_image(self):
        self.image = pygame.transform.rotate(
            pygame.image.load(f"{PROJECT_DIR}/images/Bee.png" ).convert_alpha(), 180
        )
