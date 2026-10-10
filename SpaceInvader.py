import math
import random
import pygame
screen_width = 800
screen_height = 500
Player_start_x = 370
Player_start_y= 380
Enemy_start_y_min = 50
Enemy_start_y_max= 150
Enemy_speed_x = 4
Enemy_speed_y = 40
Bullet_speed_y = 10
collision_distance = 27
pygame.init()
screen = pygame.display.setmode((screen_width , screen_height))
background = pygame.image.load('background.png')
pygame.display.set_caption('Space Invader')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
Playerimg = pygame.image.load('player.png')
Playerx = Player_start_x
Playery = Player_start_y
Playerx_change = 0
Enemyimg = []
Enemyx = []
Enemyy = []
Enemyx_change = []
Enemyy_change = []
Number_of_enemies = 6
for i in range(Number_of_enemies):
    Enemyimg.append()
    pygame.image.load('enemy.png')
    Enemyx.append(random.randint(0,screen_width - 64))
    Enemyy.append(random.randint(Enemy_start_y_min, Enemy_start_y_max))
    Enemyx_change.append(Enemy_speed_x)
    Enemyy_change.append(Enemy_speed_y)
Bulletimg = pygame.image.load('bullet.png')
Bulletx = 0
Bullety = Player_start_y
Bulletx_change = 0
Bullety_change = Bullet_speed_y
Bullet_state = "ready"
score = 0
font = pygame.font.Font('freesansbold.ttf',32)
Textx = 10
Texty = 10
overfont = pygame.font.Font('freesansbold.ttf',64)
def show_score(x,y):
    score = font.render('Score:'+ str(score),True,(255,255,255))
    screen.blit(score,(x,y))
def game_overtext():
    overtext = overfont.render('Game Over',True,(255,255,255))
    screen.blit(overtext,(200,250))
def Player(x,y):
    screen.blit(Playerimg(x,y))
def Enemy(x,y,i):
    screen.blit(Enemyimg[i],(x,y))
def Bullet(x,y):
    global Bullet_state 
    Bullet_state = "Fire"
    screen.blit(Bulletimg,(x + 16,y + 10))
def Collision(Enemyx, Enemyy, Bulletx, Bullety):
     distance = math.sqrt((Enemyx,Bulletx)**2+(Enemyy - Bullety)**2)
     return(distance < collision_distance)
Running = True
while Running:
    screen.fill((0,0,0))
    screen.blit(background(0,0))
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        Running = False
        if type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Playerx_change - 5
            if event.key == pygame.K_RIGHT:
                Playery_change = 5
            if event.key == pygame.K_SPACE and Bullet_state == "ready":
                Bulletx = Playerx
                Bullet(Bulletx, Bullety)
        if event.type == pygame.KEYUP and event.key in [pygame.KLEFT, pygame.KRIGHT]:
            Playerx_change = 0