import pygame

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((1200,800))

# Caption and Icon
pygame.display.set_caption("Art Heist")
icon = pygame.image.load('AHLogo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('GreenNinjaCharacter.png')
playerX = 600
playerY = 400
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = pygame.image.load('NinjaCharacter.png')
enemyX = 400
enemyY = 400
enemyX_change = 0.5
enemyY_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

# Game Loop
running = True
while running:

    # RGB (Red, Green, Blue)
    screen.fill((254, 254, 254))
    
    playerX += playerX_change
    enemyX += enemyX_change

    # Boundaries for both characters
    if playerX <= 0:
        playerX = 0
    elif playerX >= 1140:
        playerX = 1140

    if playerY <= 0:
        playerY = 0
    elif playerY >= 680:
        playerY = 680 

    if enemyX <= 700:
        enemyX = 700
    elif enemyX >= 1100:
        enemyX = 1100

    if enemyY <= 0:
        enemyY = 0
    elif enemyY >= 680:
        playerY = 680

    # Enemy movement
    if enemyX == 1100:
        enemyX_change = -0.5
    if enemyX == 700:
        enemyX_change = 0.5

    # Update entity locations
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                       
        # Checks keystroke for left or right
        # pygame.mouse.set_pos(400, 400)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2
                print("Left arrow")
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
                print("Right arrow")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                print("Released")
