import pygame
pygame.init()


def Instructions():

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
    myfont_Line1 = pygame.font.SysFont('Comic Sans MS', 19, bold = True)
    myfont_Line2 = pygame.font.SysFont('Comic Sans MS', 18, bold = True)
    myfont_Line3 = pygame.font.SysFont('Comic Sans MS', 17, bold = True)

    background = pygame.image.load("InstructionsTest.png")
    window.blit(background,(0,0))

    #Instructions menu that welcomes the user
    Welcome = myfont_intro.render("WELCOME", 10, Black)
    window.blit(Welcome,(150, 30))


    #Text Lines
    Line1 = "You were sent by the mafia to steal a painting"
    Line2 = "or else they kill your wife and kids." 
    Line5 = "Your goal is to avoid the gaurds"
    Line6 = "parkour on platforms in order to reach the painting."
    Line3 = "Each painting you steal will increase your" 
    Line4 = "reward from the mafia"

    #Directions Text
    Directions1 = "Up Key = jump" 
    Directions2  = "Right key = move forward"
    Directions3 = "Left key = backward"

    #Renders the story line and the intro
    Intro = myfont_Line1.render(Line1,2, yellow)
    Intro2 = myfont_Line1.render(Line2,2,yellow)

    Intro3 = myfont_Line2.render(Line3,2,white)
    Intro4 = myfont_Line2.render(Line4,2,white)

    Intro5 = myfont_Line3.render(Line5,2, white)
    Intro6 = myfont_Line3.render(Line6,2, white)

    #Renders the directions
    Display1 = myfont.render(Directions1,10, Blue)
    Display2 = myfont.render(Directions2,10, Blue)
    Display3 = myfont.render(Directions3, 10, Blue)

    #Displays the the window being built in the window with the Y-coordinates changing 
    window.blit(Intro,(35, 110))
    window.blit(Intro2,(35, 140))

    window.blit(Intro3,(35, 180))
    window.blit(Intro4,(35, 210))

    window.blit(Intro5,(35, 250))
    window.blit(Intro6,(35, 280))

    window.blit(Display1,(140, 370))
    window.blit(Display2,(140, 400))
    window.blit(Display3,(140, 430))

    #Allows for a display of the window with changes
    pygame.display.update()

    #Makes sure that the window doesn't close without something happening
    running = True 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

Instructions()




