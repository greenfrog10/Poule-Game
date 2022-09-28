from turtle import update
from bullet import Bullet
from player import *
import pygame
import window_settings
pygame.init()
screen = pygame.display.set_mode((window_settings.width,window_settings.height))
pygame.display.set_caption(window_settings.title)
pygame.display.set_icon(window_settings.icon)
player = Player("assets/hen.png",0,window_settings.height - 70)
#bullet = Bullet(0,0,player.direction)
run = True
while run:
    #bullet = Bullet(0,0,"assets/bullet.png",player.direction)
    screen.fill(window_settings.bg_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left()
            if event.key == pygame.K_RIGHT:
                player.right()
        if event.type == pygame.KEYUP:
            player.stop()
    screen.fill(window_settings.bg_color)
    player.update()
    #bullet.update()
    if player.x <= window_settings.border_left:
        player.x = window_settings.border_left
    elif player.x > window_settings.border_right:
        player.x = window_settings.border_right
    screen.blit(player.sprite,(player.x,player.y))
    #screen.blit(bullet.sprite,(bullet.x,bullet.y))
    pygame.display.update()