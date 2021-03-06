import pygame
import random

# initialize pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))

#background
background = pygame.image.load("background2.png")

#title and icon
pygame.display.set_caption("SPACE")
icon = pygame.image.load('games.png')
pygame.display.set_icon(icon)

#Adding Player
playerImg = pygame.image.load('rocket.png')

#kata tira rakhni
playerX = 370
playerY = 480
    #Movement
playerX_change=0
playerY_change=0

# Adding enemy
enemyImg = pygame.image.load("enemies.png")
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)

#increase moment speed
enemyX_change = 3
enemyY_change =40

# Adding bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change=0
bulletY_change=3

# Ready state - you can't see bullet on screen
# Fire state - bullet moving currently
bullet_state = "ready"



def player(x,y):
    #blit --> draw
    screen.blit(playerImg, (x, y))

def enemy(x,y):
    screen.blit(enemyImg, (x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+2))

#Game Loop
running = True

while running:

#RBG COLOR TO RGB for background color
    screen.fill((128, 0, 0))

# background images makes speed slow
    screen.blit(background, (0,0))

    #speed
    #playerX += 0.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed whether its right or left
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                #Increase to 0.3 if u want to increase the speed
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1

            if event.key == pygame.K_UP:
                playerY_change = -1

            if event.key == pygame.K_DOWN:
                playerY_change = 1

            if event.key == pygame.K_SPACE:
                fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change

    # creating boundaries
    if playerX <=0:
        playerX = 0
    elif playerX >=736:
        playerX=736
    if playerY <=0:
        playerY = 0
    elif playerY >=530:
        playerY=530

    #enemy movement
    enemyX += enemyX_change

    #bullet movement
    if bullet_state is "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change

    # Creating boundaries
    if enemyX <= 0:
        enemyX_change = 3
    elif enemyX >=736:
        enemyX_change = -4
        enemyY += enemyY_change

    player(playerX,playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()
