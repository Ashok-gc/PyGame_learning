import pygame

# initialize pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))

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

def player(x,y):
    #blit --> draw
    screen.blit(playerImg, (playerX, playerY))

#Game Loop
running = True

while running:

#RBG COLOR TO RGB for background color
    screen.fill((128, 0, 0))

    #speed
    #playerX += 0.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed whether its right or left
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                #Increase to 0.3 if u want to increase the speed
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1

            if event.key == pygame.K_UP:
                playerY_change = -0.1

            if event.key == pygame.K_DOWN:
                playerY_change = 0.1

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

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

    player(playerX,playerY)

    pygame.display.update()
