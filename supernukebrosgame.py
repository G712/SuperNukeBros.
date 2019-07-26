import pygame
import random
from supernukebros import Mario
from nukebro import Nuke
pygame.init()
screen_info = pygame.display.Info()

screen_size = (screen_width, screen_height) =\
    (int(screen_info.current_w * 1),
     int(screen_info.current_h * 1))



screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()





SuperMario = Mario((120, 120))
enemies = pygame.sprite.Group()
font = pygame.font.SysFont(None, 40)


def init():
    enemies.empty()
    for i in range(10):
        enemies.add(Nuke((random.randint(50, screen_width - 50),
                           random.randint(50, screen_height))))


def main():
    dead = False
    score = 0
    init()
    while True:
        score += 1/60
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    SuperMario.accel.x = 0.15
                if event.key == pygame.K_LEFT:
                    SuperMario.accel.x = -0.15
                if event.key == pygame.K_UP:
                    SuperMario.accel.y = -0.15
                if event.key == pygame.K_DOWN:
                    SuperMario.accel.y = 0.15
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    SuperMario.accel.x -= 0.15
                if event.key == pygame.K_LEFT:
                    SuperMario.accel.x += 0.15
                if event.key == pygame.K_UP:
                    SuperMario.accel.y += 0.15
                if event.key == pygame.K_DOWN:
                    SuperMario.accel.y -= 0.15


        SuperMario.update()
        enemies.update()

        player_hit = pygame.sprite.spritecollide(SuperMario, enemies, False)

        if player_hit:
            init()
            SuperMario.reset((150, 150))
            dead = True
        screen.fill((52, 235, 140))
        if not dead:
            SuperMario.draw(screen)
        enemies.draw(screen)
        text = font.render("Time not nuked: " + str(int(score)) + " seconds. ", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (200, 45)
        screen.blit(text, text_rect)
        pygame.display.flip()
        if dead:
            dead = False
            pygame.time.delay(1000)
            score = 0


if __name__ == "__main__":
    main()



