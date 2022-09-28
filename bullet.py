from turtle import right
import pygame
class Bullet:
    def __init__(self,x,y,direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.sprite_right = sprite
        self.sprite_left = pygame.transform.flip(self.sprite,False,True)
        self.sprite = pygame.image.load(self.sprite_right)
    def update(self):
        if self.direction == "Right":
            self.sprite = pygame.image.load(self.sprite_right)
        if self.direction == "Left":
            self.sprite = pygame.image.load(self.sprite_left)
            
        
        