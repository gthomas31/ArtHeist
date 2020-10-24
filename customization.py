import pygame, menu
pygame.init()

runner = menu.Running()

#function to customize colors
#draw pngs of each ninja and make them buttons 
#size of each character: (60, 120)
def custom(runner): 
    

    
    window = pygame.display.set_mode((500,500))
    pygame.display.set_caption('Art Heist')


    bg = pygame.image.load("InstructionsTest.png")
    window.blit(bg,(0,0))

    white = (0,0,0)

    myfont = pygame.font.SysFont('Comic Sans MS', 30, bold = True)
    Title = "Choose your Ninja!"
    Title_Display = myfont.render(Title, 2, white)
    window.blit(Title_Display, (120,32))

    Ninja = pygame.font.SysFont('Comic Sans MS', 15, bold = True, italic= True)
    red_Ninja =  "Red Ninja"
    Red_Display = Ninja.render(red_Ninja, 2, white)
    window.blit(Red_Display,(100, 175+50))

    pink_Ninja =  "Pink Ninja"
    Pink_Display = Ninja.render(pink_Ninja,2,white)
    window.blit(Pink_Display,(100,325+50))

    green_Ninja = "Green Ninja"
    green_Display = Ninja.render (green_Ninja,2,white)
    window.blit(green_Display, (190,250+50))

    lightblue_ninja =  "Light Blue Ninja"
    lightblue_display = Ninja.render(lightblue_ninja,2,white)
    window.blit(lightblue_display,(280,175+50)) 

    blue_ninja = "Blue Ninja"
    Blue_display = Ninja.render(blue_ninja,2,white)
    window.blit(Blue_display,(300,325+50))

    #----------------------------------------------------------------

    red = pygame.image.load("RedNewNinja.png")
    window.blit(red, (100, 100))

    pink = pygame.image.load("PinkNewNinja.png")
    window.blit(pink, (100, 250))

    lightblue = pygame.image.load("TurqNewNinja.png")
    window.blit(lightblue, (300, 100))

    blue = pygame.image.load("BlueNewNinja.png")
    window.blit(blue, (300, 250))

    green = pygame.image.load("GreenNewNinja.png")
    window.blit(green, (200, 175))



    pygame.display.update()

    charx = 60
    chary = 120

    red = False
    pink = False
    lb = False
    blue = False
    green = False

    #while runner.running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runner.changeRunning()
        elif event.type == pygame.MOUSEBUTTONDOWN:
        
            pointx, pointy = pygame.mouse.get_pos()
            #size of eaach character (60, 120)
            #red ninja
            if (100 < pointx < (100+charx)) and (100 < pointy < (100+chary)):
                print("you picked red")
                red = True
                pink = False
                lb = False
                blue = False
                green = False
                runner.running = False
            
            #pink ninja 
            elif (100 < pointx < (100 + charx)) and (250 < pointy < (250+chary)):
                print("you picked pink")
                red = False
                pink = True
                lb = False
                blue = False
                green = False
                runner.running = False

            #lightblue ninja
            elif (300 < pointx < (300+charx)) and (100 < pointy < (100+chary)):
                print("you picked light blue") 
                red = False
                pink = False
                lb = True
                blue = False
                green = False 
                runner.running = False

            #blue ninja
            elif (300 < pointx < (300+charx)) and (250 < pointy < (250+chary)): 
                print("you picked blue")
                red = False
                pink = False
                lb = False
                blue = True
                green = False
                runner.running = False

            #green ninja
            elif (200 < pointx < (200+charx)) and (175 < pointy < (175+chary)):
                print("you chose green")
                red = False
                pink = False
                lb = False
                blue = False
                green = True   
                runner.running = False          

    return red, pink, lb, blue, green
