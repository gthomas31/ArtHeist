
import pygame, menu, instructions, player, enemy, level, customization

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((1200, 800))

# Levels
nightLevel = level.Level('NightScene.png', 733)
platform1 = level.Platform(400, 650, 100, 25)
nightLevel.addPlatform(platform1, screen)

# Caption and Icon
pygame.display.set_caption("Art Heist")
icon = pygame.image.load('AHLogo.png')
pygame.display.set_icon(icon)


greenNinja = player.Player('GreenNinjaCharacter.png')
enemyNinja = enemy.Enemy('enemyCharacter.png', 400, nightLevel.groundLevel - 135)

#play_button, tutorial_button, credit_button, practice_button = menu.activemenu()

# Running class
menuRunner = menu.Running()
instructionRunner = menu.Running()
customizationRunner = menu.Running()

play_button = False
tutorial_button = False
credit_button = False
custom_button = False

#dont think this is doing anything
red = False
pink = False
lb = False
blue = False
green = False

# Game Loop
running = True
while running:
    
    if play_button == False and tutorial_button == False and credit_button == False and custom_button == False:
        play_button, tutorial_button, credit_button, custom_button = menu.activemenu(menuRunner)
        running = menuRunner.running

    if instructionRunner.running == False: 
        tutorial_button = False
        instructionRunner.running = True

    
    if customizationRunner.running == False: 
        custom_button = False
        customizationRunner.running = True
       
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        greenNinja.movement(event)
        

        
    if play_button == True:   
        enemyNinja.movement()
        # RGB (Red, Green, Blue)
        nightLevel.displayBackground(screen)

        #screen.fill((254, 254, 254))
        greenNinja.boundaries(screen, nightLevel)
        enemyNinja.boundaries(screen)
    
    elif tutorial_button == True: 
        instructions.Instructions(instructionRunner)

    elif custom_button == True: 
        filecolor = customization.custom(customizationRunner)
        greenNinja.changeImageFile(filecolor)
        





        
