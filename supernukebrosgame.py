import pygame
from supernukebros import Mario

pygame.init()
screen_info = pygame.display.Info()

screen_size = (screen_width, screen_height) =\
    (int(screen_info.current_w * 1),
     int(screen_info.current_h * 1))



screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
SuperMario = Mario((120, 120))

def main():
    while True:

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
        screen.fill((52, 235, 140))
        SuperMario.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()