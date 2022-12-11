import pygame
from player import Player

def run():

    pygame.init()
    WIDTH = 800
    HEIGHT = 734
    IMAGE_HEIGHT = 1536
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption('Blades of spaces v.0.1')

    source_bg = pygame.image.load('starfield.jpg')
    bg1 = source_bg.convert()

    screen_pos = 0

    clock = pygame.time.Clock()

    player = pygame.sprite.GroupSingle()
    player.add(Player())

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill((0,0,0))
        screen.blit(bg1,(0, -HEIGHT + screen_pos))
        screen.blit(bg1,(0, -HEIGHT - IMAGE_HEIGHT + screen_pos))

        player.draw(screen)
        player.update()


        if screen_pos == IMAGE_HEIGHT:
            screen_pos = 0

        screen_pos += 4


        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    run()
