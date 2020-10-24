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
    icon = pygame.image.load('GreenNinjaCharacter.png')
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
    playrect.set_alpha(120)
    playrect.fill((255,255,255))
    win.blit(playrect, (235,210))
    #pygame.display.update()

    #tutoral rectangle ----------------------------------------------------------------------
    tutorialrect = pygame.Surface((240, 200))
    tutorialrect.set_alpha(120)
    tutorialrect.fill((255,255,255))
    win.blit(tutorialrect, (340, 490))
    #pygame.display.update()

    #credits rectangle ----------------------------------------------------------------------
    creditsrect = pygame.Surface((200, 180))
    creditsrect.set_alpha(120)
    creditsrect.fill((255,255,255))
    win.blit(creditsrect, (800, 380))
    creditsrect.get_clip()
    #pygame.display.update()
    
    #practice rectangle ----------------------------------------------------------------------
    practicerect = pygame.Surface((260, 180))
    practicerect.set_alpha(120)
    practicerect.fill((255,255,255))
    win.blit(practicerect, (880, 125))
    pygame.display.update()
    
    
    pygame.display.update()
    return (win, playrect, tutorialrect, creditsrect, practicerect)  

    #create all button rectangles: play, tutorial, credits, practice

()   




def clicked(click, rect):

    p1 = rect.topleft
    p2 = rect.bottomright
    #0=x, 1=y
    return p1[1] > point[0] > p2[0] and p1[1] > point[1] > p2[2]

() 


def activemenu(): 

    tab, prect, trect, crect, pracrect = menulook()

    pointx, pointy = pygame.mouse.get_pos()
    press = pygame.mouse.get_pressed()
    
     #run until closed
    running = True 
    while running: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False
            #play button
            elif event.type == pygame.MOUSEBUTTONDOWN:
    
                pointx, pointy = pygame.mouse.get_pos()
    
                if  (235 < pointx < (235 + 230)) and (210 < pointy < (210+ 240)):
                    print("you're playing!!")

            #tutorial button
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                pointx, pointy = pygame.mouse.get_pos()

                if (340 < pointx < (240 + 340)) and (490 < pointy < (200 + 490)):
                    print("time for tutorial!")

            #credits button
            #elif event.type == pygame.MOUSEBUTTONDOWN and p1[1] > point[0] > p2[0] and p1[1] > point[1] > p2[2]:
                #print("ramiz did everything.")
            
            #practice button
            #elif even.type  == pygame.MOUSEBUTTONDOWN and p1[1] > point[0] > p2[0] and p1[1] > point[1] > p2[2]:
                #print("practice makes perfect")
               


()

activemenu()
     


