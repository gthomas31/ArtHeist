import pygame, menu
pygame.init()

def Instructions(runner):

    #Rgb color that will be user later in the code for the text and anything else
    yellow = (255, 255, 0)
    white = (255,255,255)
    Blue = (54,15,250)
    Black = (1,16,16)

    #Creates the instructions rectangles and also sets the background for the tutorial
    window = pygame.display.set_mode((500,500))
    pygame.display.set_caption('Art Heist')

    #Font control for the output
    myfont = pygame.font.SysFont('Comic Sans MS', 20, bold = True)
    myfont_intro = pygame.font.SysFont('Comic Sans MS', 40, bold = True)

    myfont_Line1 = pygame.font.SysFont('Comic Sans MS', 17, bold = True)
    myfont_Line2 = pygame.font.SysFont('Comic Sans MS', 16, bold = True)
    myfont_Line3 = pygame.font.SysFont('Comic Sans MS', 17, bold = True)

    background = pygame.image.load("InstructionsTest.png")
    window.blit(background,(0,0))

    #Instructions menu that welcomes the user
    Welcome = myfont_intro.render("WELCOME", 10, Black)
    window.blit(Welcome,(150, 30))


    #Text Lines
    Line1 = "During the day you spend your time at art exhibits."
    Line2 = "During the night you also spend time at art exhibits." 

    Line3 = "However, at night you become the Art Ninja Thief!"
    Line4 = "Use your elite ninja skills to steal prized art pieces."
    
    
    Line5 = "The more paintings you collect, the greater your " 
    Line6 = "collection becomes." 
    Line7 = "Be warned! The guards are ruthless!" 

    #Directions Text
    Directions1 = "SPACE = jump" 
    Directions2  = "Right key = move forward"
    Directions3 = "Left key = backward"

    #Renders the story line and the intro
    Intro = myfont_Line1.render(Line1,2, yellow)
    Intro2 = myfont_Line1.render(Line2,2,yellow)

    Intro3 = myfont_Line2.render(Line3,2,white)
    Intro4 = myfont_Line2.render(Line4,2,white)

    Intro5 = myfont_Line3.render(Line5,2, white)
    Intro6 = myfont_Line3.render(Line6,2, white)
    Intro7 = myfont_Line3.render(Line7,2,white)

    #Renders the directions
    Display1 = myfont.render(Directions1,10, Blue)
    Display2 = myfont.render(Directions2,10, Blue)
    Display3 = myfont.render(Directions3, 10, Blue)

    #Displays the the window being built in the window with the Y-coordinates changing 
    window.blit(Intro,(37, 110))
    window.blit(Intro2,(37, 140))\

    window.blit(Intro5,(40, 250))
    window.blit(Intro6,(200, 280))

    window.blit(Intro3,(40, 180))
    window.blit(Intro4,(40, 210))

    window.blit(Intro7, (172, 310))

    window.blit(Display1,(140, 370))
    window.blit(Display2,(140, 400))
    window.blit(Display3,(140, 430))

    #Allows for a display of the window with changes
    pygame.display.update()

    #Makes sure that the window doesn't close without something happening
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runner.changeRunning()