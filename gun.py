import pygame 
class Gun:
    def __init__(self,sprite,x,y):
        self.x = x
        self.y = y
        self.sprite = pygame.image.load(sprite)
        