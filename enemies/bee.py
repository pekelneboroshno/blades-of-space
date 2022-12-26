import pygame
from .base import Enemy, PROJECT_DIR

import sys
from pathlib import Path

PROJECT_DIR = str(Path.cwd())
sys.path.append(PROJECT_DIR)


class Bee(Enemy):

    def set_image(self):
        self.image = pygame.transform.rotate(
            pygame.image.load(f"{PROJECT_DIR}/images/Bee.png" ).convert_alpha(), 180
        )
