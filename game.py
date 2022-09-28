from turtle import update
from bullet import Bullet
from gun import Gun
from player import Player
import pygame
import window_settings
pygame.init()
screen = pygame.display.set_mode((window_settings.width,window_settings.height))
pygame.display.set_caption(window_settings.title)
pygame.display.set_icon(window_settings.icon)
player = Player("assets/hen.png",0,window_settings.height - 70)
gun = Gun("assets/gun_down_right.png",player.x + 60,player.y) 
bullet = Bullet(gun.x,gun.y,player.direction,player.gun)
run = True
while run:
    if bullet.fire == False:
        bullet = Bullet(gun.x,gun.y,player.direction,player.gun)
    screen.fill(window_settings.bg_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left()
            if event.key == pygame.K_RIGHT:
                player.right()
            if event.key == pygame.K_SPACE:
                bullet.shoot()
            if event.key == pygame.K_UP:
                player.raise_gun()
            if event.key == pygame.K_DOWN:
                player.lower_gun()
        if event.type == pygame.KEYUP:
            player.stop()
    screen.fill(window_settings.bg_color)
    player.update()
    bullet.update()
    if player.x <= window_settings.border_left:
        player.x = window_settings.border_left
    elif player.x > window_settings.border_right:
        player.x = window_settings.border_right
    if bullet.x <= window_settings.border_left:
        bullet.fire = False
    elif bullet.x > window_settings.border_right:
        bullet.fire = False
    if player.gun == "Down":
        if player.direction == "Right":
            gun.sprite = "assets/gun_down_right.png"
        elif player.direction == "Left":
            gun.sprite = "assets/gun_down_left.png"
    if player.gun == "Up":
        if player.direction == "Right":
            gun.sprite = "assets/gun_up_right.png"
        elif player.direction == "Left":
            gun.sprite = "assets/gun_up_left.png"
    screen.blit(player.sprite,(player.x,player.y))
    if player.direction == "Right":
        gun.x = player.x + 60
        screen.blit(pygame.image.load(gun.sprite),(gun.x,gun.y))
    if player.direction == "Left":
        gun.x = player.x - 30
        screen.blit(pygame.image.load(gun.sprite),(gun.x,gun.y))
    if bullet.y < 0:
        bullet.fire = False
    if bullet.fire:
        screen.blit(bullet.sprite,(bullet.x,bullet.y))
    pygame.display.update()
