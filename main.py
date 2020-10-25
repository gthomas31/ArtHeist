
import pygame, menu, instructions, player, enemy, level, customization, score, painting

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((1200, 800))

# Score
score = score.ScoreCounter(0)

# Night Level
nightLevel = level.Level('NightScene.png', 733)
platform1 = level.Platform(1028, 522, 142, 29)
platform2 = level.Platform(885, 622, 134, 29)
nightLevel.addPlatform(platform1, screen)
nightLevel.addPlatform(platform2, screen)
enemyNinja = enemy.Enemy('enemyCharacter.png', 200, nightLevel.groundLevel - 120, 400, 800)
painting1 = painting.Painting('Painting.png', 1081, 522 - 51, screen)
nightLevel.addPainting(painting1, screen)

# Museum Entrance
# entranceLevel = level.Level(, )

# Caption and Icon
pygame.display.set_caption("Art Heist")
icon = pygame.image.load('AHLogo.png')
pygame.display.set_icon(icon)


greenNinja = player.Player('GreenNewNinja.png')


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
        if score.currentScore == 0:
            enemyNinja.movement(greenNinja)
            # RGB (Red, Green, Blue)
            nightLevel.displayBackground(screen)
            score.score(screen, score.currentScore)
            #screen.fill((254, 254, 254))
            greenNinja.boundaries(screen, nightLevel)
            enemyNinja.boundaries(screen)
            for painting in nightLevel.paintingList:
                if (painting.collision(greenNinja)):
                    score.currentScore += 1
        elif score.currentScore == 1:
            print("Level 2")
        
    
    elif tutorial_button == True: 
        Instructions.Instructions(instructionRunner)

    elif custom_button == True: 
        filecolor = customization.custom(customizationRunner)
        greenNinja.changeImageFile(filecolor)
        





        
