import pygame
import random
import math
pygame.init()
screen=pygame.display.set_mode((800, 800))
pygame.display.set_caption("Kittu space")
icon=pygame.image.load('space.png')
pygame.display.set_icon(icon)
playerimg=pygame.image.load('player.png')
playerimg=pygame.transform.scale(playerimg, (120,120))
backgroundimg=pygame.image.load('background.png')
backgroundimg=pygame.transform.scale(backgroundimg,(800,800))
crashsound=pygame.mixer.Sound('crash.wav')
mainsound=pygame.mixer.Sound('mainsound.wav')

playerX=350
playerY=550
enemyimg=pygame.image.load('enemy.png')
enemyimg=pygame.transform.scale(enemyimg, (60,60))
enemyX=random.randint(0,800)
enemyY=50
bulletimg=pygame.image.load('bullet.png')
bulletimg=pygame.transform.scale(bulletimg,(40,40))
def player(x,y):
    screen.blit(playerimg, (x,y))
def enemy(x,y):
    screen.blit(enemyimg, (x,y))
def bullet(x,y):
    screen.blit(bulletimg, (x+40,y))
def iscollision(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt(math.pow(enemyx-bulletx,2)+math.pow(enemyy-bullety,2))
    if distance<20:
        return True
    return False
run=True
changeX=0
changeY=0
enemychangeX=4
enemychangeY=0
state="ready"
bullet_x=0
bullet_y=playerY
bullets=[]
mainsound.set_volume(0.01)
while run:
    mainsound.play()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.display.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                changeX=-5
            if event.key==pygame.K_RIGHT:
                changeX=5
            if event.key==pygame.K_UP:
                changeY=-5
            if event.key==pygame.K_DOWN:
                changeY=5
            if event.key==pygame.K_SPACE:
                state="fired"
                bullet_x=playerX
                bullets.append([bullet_x,playerY])
        if event.type==pygame.KEYUP:
            changeX=0
            changeY=0
    screen.blit(backgroundimg,(0,0))
    playerX+=changeX
    playerY+=changeY
    if playerX<=-38:
        playerX=-38
    elif playerX>=718:
        playerX=718
    if enemyX<=-12:
        enemychangeX=4
        enemyY+=20
    elif enemyX>=740:
        enemychangeX=-4
        enemyY+=20
    enemyX+=enemychangeX
    player(playerX,playerY)
    enemy(enemyX,enemyY)
    if state=="fired":
        for i in range(len(bullets)):
            bullets[i][1]-=9
            bullet(bullets[i][0],bullets[i][1])
            if iscollision(enemyX,enemyY,bullets[i][0],bullets[i][1]):
                print(1)
                enemyY=50
                mainsound.stop()
                crashsound.play()
    pygame.display.update()
mainsound.stop()