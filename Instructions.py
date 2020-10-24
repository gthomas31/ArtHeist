def Instructions():
    import pygame
    pygame.init()

    #Rgb colors that will be user later in the code for the text and anything else
    white = (255,255,255)
    red = (255,0,0)

    #Creates the instructions rectangles
    window = pygame.display.set_mode((500,500))
    pygame.display.set_caption('Art Heist')
    myfont = pygame.font.SysFont('Comic Sans MS', 15)

    #Instructions menu that welcomes the user
    Intro = myfont.render("WELCOME", 2, white)
    window.blit(Intro,(210, 230))

    #Text Lines
    Line1 = "You were sent by the mafia to steal a painting or else they kill your" 
    Line2 = "wife and kids. Your goal is to avoid the gaurds, parkour on platforms in"
    Line3 = "order to reach the painting. Each painting you steal will increase your" 
    Line4 = "reward from the mafia"

    #Directions Text
    Directions1 = "Press Up or space bar Key to jump, Press right key to move forward"
    Directions2 = "Press left key to move the character backward"

    #Renders the story line and the intro
    Intro = myfont.render(Line1,2, white)
    Intro2 = myfont.render(Line2,2,white)
    Intro3 = myfont.render(Line3,2,white)
    Intro4 = myfont.render(Line4,2,white)

    #Renders the directions
    Display1 = myfont.render(Directions1,2, white)
    Display2 = myfont.render(Directions2,2, white)

    #Displays the the window being built in the window with the Y-coordinates changing 
    window.blit(Intro,(10, 10))
    window.blit(Intro2,(10, 40))
    window.blit(Intro3,(10, 70))
    window.blit(Intro4,(10, 100))
    window.blit(Display1,(10, 350))
    window.blit(Display2,(10, 380))
    pygame.display.update()

    #Sets the background for the tutorial
    background = pygame.image.load("InstructionsTest.png")
    window.blit(background(0,0))

    #Makes sure that the window doesn't close without something happening
    running = True 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

Instructions()




