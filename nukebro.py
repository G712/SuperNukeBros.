import pygame
from object import Object
import random

class Nuke(Object):
    def __init__(self, pos):
        super().__init__("nukebro.png", pos)
        self.image = pygame.transform.smoothscale(self.image, (60, 30))
        self.accel = pygame.math.Vector2()


    def update(self):
        self.accel = (random.uniform(-0.3, 0.3),random.uniform(-0.3, 0.3))
        self.speed += self.accel
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
        super().update()

