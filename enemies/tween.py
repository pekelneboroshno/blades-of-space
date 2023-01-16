import pygame
from .base import Enemy
from blades_of_space.settings import PROJECT_DIR, WIDTH


class AIRight:

    def move(self) -> tuple:
        return (-1, 0)


class AILeft:

    def move(self) -> tuple:
        return (1, 0)


class Twin(Enemy):

    ai_left = AILeft()
    ai_right = AIRight()

    RIGHT_START_POSITION = (WIDTH, 0)
    LEFT_START_POSITION = (-230, 0)

    def __init__(self, timeout = 0, position: tuple = RIGHT_START_POSITION, config = ai_right):
        self.timeout = timeout
        super().__init__(config)
        self.velocity = 2
        self.rect.x, self.rect.y = position

    def move(self):
        self.timeout -= 1
        if self.timeout < 0:
            super().move()

    def set_image(self):
        self.image = pygame.transform.rotate(
            pygame.image.load(f"{PROJECT_DIR}/images/Twin.png" ).convert_alpha(), 180
        )
        self.image = pygame.transform.rotozoom(self.image, 1.0, 1.3)
