#starting menu for art heist - ramiz

import pygame

#initialize pygame - FOR TEST PURPOSES, THIS WILL BE IN MAIN LATER
pygame.init()

#defining menu
def menulook(): 

    #create the window
    win = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Art Heist")
    #INSERT WINDOW LOGO
    icon = pygame.image.load('AHLogo.png')
    pygame.display.set_icon(icon)

     #add the menu image 
    menuscreen = pygame.image.load('MenuScreen.png')
    centerx = 0
    centery = 0
    win.blit(menuscreen, (centerx, centery))
    pygame.display.update()

    #create all invisible rectangles - CHANGE SIZE TO WHERE THE BUTTONS ARE AND OPACITY TO 0
    #pygame.draw.rect(win, (0, 0, 0), (235,210, 230, 240))

    #play rectangle ------------------------------------------------------------------------
    playrect = pygame.Surface((230, 240))
    playrect.set_alpha(0)
    playrect.fill((255,255,255))
    win.blit(playrect, (235,210))
    #pygame.display.update()

    #tutoral rectangle ----------------------------------------------------------------------
    tutorialrect = pygame.Surface((240, 200))
    tutorialrect.set_alpha(0)
    tutorialrect.fill((255,255,255))
    win.blit(tutorialrect, (340, 490))
    #pygame.display.update()

    #credits rectangle ----------------------------------------------------------------------
    creditsrect = pygame.Surface((200, 180))
    creditsrect.set_alpha(0)
    creditsrect.fill((255,255,255))
    win.blit(creditsrect, (800, 380))
    creditsrect.get_clip()
    #pygame.display.update()
    
    #practice rectangle ----------------------------------------------------------------------
    practicerect = pygame.Surface((260, 180))
    practicerect.set_alpha(0)
    practicerect.fill((255,255,255))
    win.blit(practicerect, (880, 125))
    pygame.display.update()
    
    
    pygame.display.update()
    #return (win, playrect, tutorialrect, creditsrect, practicerect)  

    #create all button rectangles: play, tutorial, credits, practice

()   


class Running:

    def __init__(self):
        self.running = True

    def changeRunning(self):
        self.running = False

def activemenu(runningClass):

    menulook()

    pointx, pointy = pygame.mouse.get_pos()

    #initializing variables
    play = False
    tutorial = False
    credit = False
    colorcust = False
    
     #run until closed
    
    #while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            runningClass.changeRunning()
        #play button
        elif event.type == pygame.MOUSEBUTTONDOWN:

            pointx, pointy = pygame.mouse.get_pos()
            
            #play button
            if  (235 < pointx < (235 + 230)) and (210 < pointy < (210+ 240)):
                #print("youre playing")
                play = True
                tutorial = False
                credit = False
                colorcust = False
            
            #tutorial
            elif (340 < pointx < (240 + 340)) and (490 < pointy < (200 + 490)):
                #print("time for tutorial!")
                play = False
                tutorial = True
                credit = False
                colorcust = False

            #credits
            elif (800 < pointx < (800 + 200)) and (380 < pointy < (380 + 180)):
                #print("all miz")
                play = False
                tutorial = False
                credit = True
                colorcust = False

            #colorcustomization
            elif (880 < pointx < (880 + 260)) and (125 < pointy < (125 + 180)):
                #print("you want to customize")
                play = False
                tutorial = False
                credit = False
                colorcust = True
    
    
    return play, tutorial, credit, colorcust




()

     


