import pygame
from player import Player, LASSERS, Laser
from enemy import Enemy
from explosion import Explosion


def process_collision(enemies: Enemy, lasser: Laser, win):
    for enemy in enemies:
        if pygame.sprite.collide_rect(enemy, lasser):
            enemies.empty()
            return True


def draw_explosions(explosions: list[Explosion], win):
    for explosion in explosions:
        explosion.draw(win)


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

    enemy = pygame.sprite.GroupSingle()
    enemy.add(Enemy())

    explosions = []

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

        enemy.draw(screen)
        enemy.update()

        for lasser in LASSERS:
            lasser.draw(screen)

            hit = process_collision(enemy, lasser, screen)
            if hit:
                explosions.append(Explosion(lasser.rect.x, lasser.rect.y))


        draw_explosions(explosions, screen)

        if screen_pos == IMAGE_HEIGHT:
            screen_pos = 0

        screen_pos += 4

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    run()
