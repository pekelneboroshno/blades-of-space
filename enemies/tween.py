import pygame
from .base import Enemy
from blades_of_space.settings import PROJECT_DIR, WIDTH
from blades_of_space.explosion import Explosion


class AIRight:

    def move(self) -> tuple:
        return (-1, 0.7)


class AILeft:

    def move(self) -> tuple:
        return (1, 0.7)


class CirclingAI:

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

    ai_left = AILeft()
    ai_right = AIRight()
    ai_circling = CirclingAI()

    RIGHT_START_POSITION = (WIDTH, 0)
    LEFT_START_POSITION = (-230, 0)


    def __init__(self, timeout = 0, position: tuple = RIGHT_START_POSITION, config = ai_right):
        self.timeout = timeout
        super().__init__(config)
        self.velocity = 2
        self.rect.x, self.rect.y = position
        self.life = 10

    def hit(self):
        self.life -= 1
        if self.life <= 0:
            self.kill()

    def move(self):
        self.timeout -= 1
        if self.timeout < 0:
            super().move()

        if (SCREEN_MIDDLE - 250 <= self.rect.x <= SCREEN_MIDDLE + 30) and not isinstance(self.ai, CirclingAI):
            self.ai = self.ai_circling

    def set_image(self):
        self.image = pygame.transform.rotate(
            pygame.image.load(f"{PROJECT_DIR}/images/Twin.png" ).convert_alpha(), 180
        )
        self.image = pygame.transform.rotozoom(self.image, 1.0, 1.3)
