
import pygame, menu, instructions, player, enemy

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

#play_button, tutorial_button, credit_button, practice_button = menu.activemenu()

# Running class
menuRunner = menu.Running()
instructionRunner = menu.Running()

play_button = False
tutorial_button = False
credit_button = False
practice_button = False

# Game Loop
running = True
while running:


    
    if play_button == False and tutorial_button == False and credit_button == False and practice_button == False:
        play_button, tutorial_button, credit_button, practice_button = menu.activemenu(menuRunner)
        running = menuRunner.running

    if instructionRunner.running == False: 
        tutorial_button = False;
        instructionRunner.running = True
       
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        greenNinja.movement(event)
        enemyNinja.movement()

        
    if play_button == True:   
        # RGB (Red, Green, Blue)
        nightscene = pygame.image.load("NightScene.png")
        screen.blit(nightscene, (0,0))

        #screen.fill((254, 254, 254))
        greenNinja.boundaries(screen)
        enemyNinja.boundaries(screen)
    
    elif tutorial_button == True: 
        instructions.Instructions(instructionRunner)




        
