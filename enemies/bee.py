import pygame
from .base import Enemy
from blades_of_space.settings import PROJECT_DIR

class Bee(Enemy):

    def set_image(self):
        self.image = pygame.transform.rotate(
            pygame.image.load(f"{PROJECT_DIR}\\images\\Bee.png" ).convert_alpha(), 180
        )
