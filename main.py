import os
import pygame
from pygame.locals import *
import random
import sys

#initialize pygame
pygame.init()

#set size of screen
size = width, height = (640, 420)
running = True
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Escape!")

#load images
bg = pygame.image.load(os.path.join("Assets","bg.png"))
blob1 = pygame.transform.scale(pygame.image.load(os.path.join("Assets","blob_rest.png")), (80,56))
blob2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets","blob_moving.png")), (80,56))
enemy = pygame.transform.scale(pygame.image.load(os.path.join("Assets","enemy.png")), (64,64))
heart_1 = pygame.transform.scale(pygame.image.load(os.path.join("Assets","heart_1.png")), (64,64))
heart_2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets","heart_2.png")), (64,64))
heart_3 = pygame.transform.scale(pygame.image.load(os.path.join("Assets","heart_3.png")), (64,64))
dead = pygame.transform.scale(pygame.image.load(os.path.join("Assets","heart_4.png")), (64,64))

#game variables
blob_x = width/2
blob_y = height - 60
blob_speed = 0.25
blob_width = 80
blob_height = 56
enemy_speed = 5
enemy_x = 0
enemy_y = 0
enemy_width = 64
enemy_height = 64
level = 1
count = 0
lives = 3
score = 0
font = pygame.font.SysFont(None,50)
gameover=False
gameover_time=0
player = blob1
score_text = "Score : " + str(score)

#collision variables
player_hitbox = player.get_rect()
player_hitbox.x = blob_x
player_hitbox.y = blob_y
enemy_hitbox = enemy.get_rect()


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
        while True:
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()
                    
            gameover=True
            text = font.render("GAME OVER", True, (255,255,255))
            screen.blit(text, (width/2 - 110,height/2))
            text = font.render(score_text, True, (255,255,255))
            screen.blit(text, (width - 185,10))
            pygame.display.update()

            
    if (enemy_y > height):
        count += 1                #if enemy falls down without hitting blob
        score += 1
        score_text = "Score : " + str(score)
        enemy_y = -500          #offset height
        enemy_x = random.randint(10, width - enemy_width)     #generate random width for next spawn
        enemy_hitbox.x = enemy_x
        if count == 5:
            level = 2
        if count == 10:
            level = 3
        if count == 15:
            level = 4
        if count == 20:
            level = 5
        if count == 30:
            while True:
                for event in pygame.event.get():
                    keys = pygame.key.get_pressed()
                    if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                        pygame.quit()
                        sys.exit()
                        
                gameover=True
                text = font.render("YOU WIN!!", True, (255,255,255))
                screen.blit(text, (width/2 - 110,height/2))
                text = font.render(score_text, True, (255,255,255))
                screen.blit(text, (width - 185,10))
                pygame.display.update()

    #getting key interaction from user
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and blob_x > 0:
        blob_x -= blob_speed
        player_hitbox.x = blob_x
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and blob_x < width - blob_width:
        blob_x += blob_speed
        player_hitbox.x = blob_x
    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_a] or keys[pygame.K_d]:
        screen.blit(blob2, (blob_x, blob_y))
        player = blob2
    else:
        screen.blit(blob1, (blob_x, blob_y))
        player = blob1

    #levels
    text = font.render(score_text, True, (255,255,255))
    screen.blit(text, (width - 185,10))
    if level == 1:
        enemy_y+=0.1
        enemy_hitbox.y = enemy_y
    if level == 2:
        enemy_y+=0.175
        enemy_hitbox.y = enemy_y
    if level == 3:
        enemy_y+=0.25
        enemy_hitbox.y = enemy_y
    if level == 4:
        enemy_y+=0.35
        enemy_hitbox.y = enemy_y
    if level == 5:
        enemy_y+=0.4
        enemy_hitbox.y = enemy_y


    #collision control block
    if player_hitbox.colliderect(enemy_hitbox):
        lives-=1
        enemy_y = 500


    #checking for exit condition
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    pygame.display.update()

pygame.quit()