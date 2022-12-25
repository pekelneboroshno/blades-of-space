import pygame


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
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.rotate(
            pygame.image.load('enemy1.png').convert_alpha(), 180
        )
        self.rect : pygame.Rect = self.image.get_rect(midbottom = (400, 150))
        self.move_speed = 3
        self.ai = AI()
        self.velocity = 2

    def move(self):
        x, y = self.ai.move()
        self.rect.x += x * self.velocity
        self.rect.y += y * self.velocity

    def update(self):
        self.move()
