import os
import pygame
from pygame.locals import *
import random

#initialize pygame
pygame.init()

#set size of screen
size = width, height = (640, 420)
running = True
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Escape!")

#load images
bg = pygame.image.load(os.path.join("Assets","bg.png"))
blob1 = pygame.transform.scale(pygame.image.load(os.path.join("Assets","blob_rest.png")), (128,128))
blob2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets","blob_moving.png")), (128,128))
enemy = pygame.transform.scale(pygame.image.load(os.path.join("Assets","enemy.png")), (64,64))
heart_1 = pygame.image.load(os.path.join("Assets","heart_1.png"))
heart_2 = pygame.image.load(os.path.join("Assets","heart_2.png"))
heart_3 = pygame.image.load(os.path.join("Assets","heart_3.png"))
dead = pygame.image.load(os.path.join("Assets","heart_4.png"))

#game variables
blob_x = width/2
blob_y = height - 120
blob_speed = 0.25
blob_width = 128
blob_height = 128
enemy_speed = 5
enemy_x = 0
enemy_y = 0
enemy_width = 64
enemy_height = 64
level = 0
count = 0
lives = 3
score = 0
font = pygame.font.SysFont(None,30)



while running:
    
    screen.blit(bg, (0, 0))
    screen.blit(enemy, (enemy_x, enemy_y))

    if lives == 3:
        screen.blit(heart_1, (0, 0))
    if lives == 2:
        screen.blit(heart_2, (0, 0))
    if lives == 1:
        screen.blit(heart_3, (0, 0))
    if lives == 0:
        screen.blit(dead, (0, 0))


    if (enemy_y > height):      #if enemy falls down without hitting blob
        enemy_y = -500          #offset height
        enemy_x = random.randint(10, width - enemy_width)      #generate random width for next spawn
    

    #getting key interaction from user
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and blob_x > 0:
        blob_x -= blob_speed
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and blob_x < width - blob_width:
        blob_x += blob_speed
    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_a] or keys[pygame.K_d]:
        screen.blit(blob2, (blob_x, blob_y))
    else:
        screen.blit(blob1, (blob_x, blob_y))

    #checking for exit condition
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    enemy_y+=0.1
    pygame.display.update()
    
pygame.quit()