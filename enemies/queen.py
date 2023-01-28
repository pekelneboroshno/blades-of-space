import pygame

from .base import Enemy
from ..weapons import VeryBigLazer

from blades_of_space.settings import PROJECT_DIR, WIDTH


class Static:

    def move(self) -> tuple:
        return (0, 0)


class Queen(Enemy):


    def __init__(self, timeout = 0):

        self.timeout = timeout
        super().__init__(Static())
        self.velocity = 2
        self.hp = 30
        self.lazers = pygame.sprite.Group()

        START_POSITION = (WIDTH // 2 - self.rect.height // 3, 50)

        self.rect.x, self.rect.y = START_POSITION

    def update(self, screen):
        super().update()
        self.shoot()

        self.lazers.draw(screen)
        self.lazers.update()

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
        self.timeout -= 1
        if self.timeout < 0:
            super().move()

    def set_image(self):
        self.image = pygame.transform.rotate(
            pygame.image.load(f"{PROJECT_DIR}/images/Queen.png" ).convert_alpha(), 180
        )
        self.image = pygame.transform.rotozoom(self.image, 1.0, 1.2)
