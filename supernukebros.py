import pygame
from object import Object

class Mario(Object):
    def __init__(self, pos):
        super().__init__("mario.png", pos)
        self.image = pygame.transform.smoothscale(self.image, (30, 30))
        self.accel = pygame.math.Vector2(0, 0)

    def update(self):
        self.speed += self.accel
        if (self.accel.length() == 0):
            self.speed *= 0.95
        elif (self.accel.length() > 10):
            self.speed.scale_to_length(10)
        super().update()

        screeninfo = pygame.display.Info()
        width = screeninfo.current_w
        height = screeninfo.current_h
        if self.rect.right > width:
            self.speed.x *= -1
        if self.rect.left < 0:
            self.speed.x *= -1
        if self.rect.top < 0:
            self.speed.y *= -1
        if self.rect.bottom > height:
            self.speed.y *= -1


    def reset(self, pos):
        self.rect.center = pos
        self.image.set_alpha(0)