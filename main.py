import pygame
import player

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((1200,800))

# Caption and Icon
pygame.display.set_caption("Art Heist")
icon = pygame.image.load('AHLogo.png')
pygame.display.set_icon(icon)

greenNinja = player.Player('GreenNinjaCharacter.png')

# Enemy
enemyImg = pygame.image.load('NinjaCharacter.png')
enemyX = 400
enemyY = 400
enemyX_change = 0.5
enemyY_change = 0

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

# Game Loop
running = True
while running:

    # RGB (Red, Green, Blue)
    screen.fill((254, 254, 254))
    
    enemyX += enemyX_change

    # Boundaries for both characters
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
    enemy(enemyX, enemyY)
    pygame.display.update()

    greenNinja.boundaries(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        greenNinja.movement(event)