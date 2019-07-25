import pygame
from object import Object

class Mario(Object):
    def __init__(self, pos):
        super().__init__("mario.png", pos)
        self.image = pygame.transform.smoothscale(self.image, (70, 70))
        self.accel = pygame.math.Vector2(0, 0)

    def update(self):
        #if self.speed.length_squared() != 0:
            #pygame.math.Vector2.scale_to_length(20)
        self.speed += self.accel

        super().update()
        #screeninfo = pygame.display.Info()
        #self.image_rect.move_ip(self.Speedy)
        #width = screeninfo.current_w
        #height = screeninfo.current_h
        #if self.image_rect.right > width:
            #self.Speedy.x *= -1
        #if self.image_rect.left < 0:
            #self.Speedy.x *= -1
        #if self.image_rect.top < 0:
            #self.Speedy.y *= -1
        #if self.image_rect.bottom > height:
            #self.Speedy.y *= -1