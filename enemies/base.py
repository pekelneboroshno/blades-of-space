import pygame

PROJECT_DIR = "/home/alex/projects/pygame_games/blades_of_space"


class AI:

    def __init__(self):
        self.counter = 400

    def rectangle_move(self) -> tuple:

        if self.counter == 0:
            self.counter = 400

        self.counter -= 1

        while True:

            if self.counter >= 300:
                return (1, 0)
            elif self.counter >= 200:
                return (0, 1)
            elif self.counter >= 100:
                return (-1, 0)
            elif self.counter >= 0:
                return (0, -1)

    def move(self):
        return self.rectangle_move()


class Enemy(pygame.sprite.Sprite):

    def set_image(self):
        self.image = pygame.transform.rotate(
            pygame.image.load('enemy1.png').convert_alpha(), 180
        )

    def __init__(self, screen_x: int = 400, screen_y: int = 150):
        self.set_image()
        self.rect : pygame.Rect = self.image.get_rect(midbottom = (screen_x, screen_y))
        self.move_speed = 3
        self.ai = AI()
        self.velocity = 2
        super().__init__()

    def move(self):
        x, y = self.ai.move()
        self.rect.x += x * self.velocity
        self.rect.y += y * self.velocity

    def update(self):
        self.move()
