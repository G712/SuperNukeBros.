import pygame
from object import Object

class Nuke(Object):
    def __init__(self, pos):
        super().__init__("nukebro.png", pos)
        self.image = pygame.transform.smoothscale(self.image, (140, 80))
        self.accel = pygame.math.Vector2()

    def update(self):
        super().update()