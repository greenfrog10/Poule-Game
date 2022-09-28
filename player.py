import pygame
class Player:
    def __init__(self,sprite,x,y):
        self.x = x
        self.y = y
        self.gun = "Down"
        self.x_change = 0
        self.sprite_left = pygame.image.load(sprite)
        self.sprite_right = pygame.transform.flip(self.sprite_left,True,False)
        self.sprite = self.sprite_right
        self.direction = "Right"
    def right(self):
        self.sprite = self.sprite_right
        self.x_change = 0.3
        self.direction = "Right"
    def left(self):
        self.sprite = self.sprite_left
        self.x_change = -0.3
        self.direction = "Left"
    def lower_gun(self):
        self.gun = "Down"
    def raise_gun(self):
        self.gun = "Up"
    def update(self):
        self.x += self.x_change
    def stop(self):
        self.x_change = 0
