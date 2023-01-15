import pygame

class Background:

    def __init__(self):
        from blades_of_space.settings import PROJECT_DIR
        self.height = 1536
        self.image = pygame.image.load(PROJECT_DIR + 'starfield.jpg').convert()
        self.screen_pos = 0

    def custom_update(self, screen, screen_height):
        screen.blit(self.image,(0, -screen_height + self.screen_pos))
        screen.blit(self.image,(0, -screen_height - self.height + self.screen_pos))

        if self.screen_pos == self.height:
            self.screen_pos = 0

        self.screen_pos += 4
