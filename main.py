import pygame

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((1200,800))

# Caption and Icon
pygame.display.set_caption("Art Heist")
icon = pygame.image.load('')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('')
playerX = 600
playerY = 400
playerX_change = 0
playerY_change = 0

def player():
    screen.blit(playerImg, (playerX, playerY))

# Game Loop
running = True
while running:

    # RGB (Red, Green, Blue)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Checks keystroke for left or right
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
                playerX_change = -0.2
            if event.type == pygame.K_RIGHT:
                playerX_change = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change  

    if playerX <= 0:
        playerX = 0
    elif playerX >= 1140:
        playerX = 1140

    if playerY <= 0:
        playerY = 0
    elif playerY >= 680:
        playerY = 680          
         
    player(playerX, playerY)
    pygame.display.update()