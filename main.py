import pygame
import player
import enemy

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((1200, 800))

# Caption and Icon
pygame.display.set_caption("Art Heist")
icon = pygame.image.load('AHLogo.png')
pygame.display.set_icon(icon)

greenNinja = player.Player('GreenNinjaCharacter.png')
enemyNinja = enemy.Enemy('NinjaCharacter.png')

# Game Loop
running = True
while running:

    # RGB (Red, Green, Blue)
    screen.fill((254, 254, 254))

    greenNinja.boundaries(screen)
    enemyNinja.boundaries(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        greenNinja.movement(event)
        enemyNinja.movement()