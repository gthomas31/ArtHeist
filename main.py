
import pygame, menu, instructions, player, enemy, level, customization, score, painting, time

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
darkMuseum = level.Level2(700)
platform3 = level.Platform(257, 595, 110, 31)
darkMuseum.addPlatform(platform3, screen)

platform4 = level.Platform(78, 500, 108, 35)
platform5 = level.Platform(266, 411, 108, 34)
platform6 = level.Platform(430, 316, 440, 35)
platform7 = level.Platform(965, 248, 153, 34)
darkMuseum.addPlatform(platform4, screen)
darkMuseum.addPlatform(platform5, screen)
darkMuseum.addPlatform(platform6, screen)
darkMuseum.addPlatform(platform7, screen)
painting2 = painting.Painting('Painting.png', 1020, 250 - 51, screen)
darkMuseum.addPainting(painting2, screen)
enemyNinjaTwo = enemy.Enemy('enemyCharacter.png', 440, 316 - 120, 435, 830)


# Caption and Icon
pygame.display.set_caption("Art Heist")
icon = pygame.image.load('AHLogo.png')
pygame.display.set_icon(icon)


ninja = player.Player('GreenNewNinja.png')


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
        ninja.movement(event)
        

        
    if play_button == True:
        if ninja.level == 1:
            enemyNinja.movement(ninja)
            # RGB (Red, Green, Blue)
            nightLevel.displayBackground(screen)
            score.score(screen, score.currentScore)
            #screen.fill((254, 254, 254))
            ninja.boundaries(screen, nightLevel)
            enemyNinja.boundaries(screen)
            for painting in nightLevel.paintingList:
                if (painting.collision(ninja)):
                    nightLevel.removePaintings()
                    nightLevel.removePlatforms()
                    score.currentScore += 1
                    ninja.level = 2
                    enemyNinja.kill()
                    pygame.display.update()

        elif (ninja.level == 2):
            darkMuseum.displayBackground(screen)
            score.score(screen, score.currentScore)
            ninja.boundaries(screen, darkMuseum)
            enemyNinjaTwo.movement(ninja)
            enemyNinjaTwo.boundaries(screen)
            pygame.display.update()
            for painting in darkMuseum.paintingList:
                if (painting.collision(ninja)):
                    darkMuseum.removePaintings()
                    nightLevel.removePlatforms()
                    score.currentScore += 1
                    ninja.level = 3
                    enemyNinjaTwo.kill()
                    pygame.display.update()
        
        elif ninja.level == 3:
            print("level 3")

           
        
    
    elif tutorial_button == True: 
        instructions.Instructions(instructionRunner)

    elif custom_button == True: 
        filecolor = customization.custom(customizationRunner)
        ninja.changeImageFile(filecolor)
        





        
