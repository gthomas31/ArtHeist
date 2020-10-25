import pygame
pygame.init()

def credits(runner): 

    win = pygame.display.set_mode((500, 500))
    creditimg = pygame.image.load("Credits.png")
    win.blit(creditimg, (0, 0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runner.changeRunning()
