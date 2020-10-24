import pygame

class Level:
    
    def __init__(self, imgFile):
        self.img = imgFile

class Platform:

    def __init__(self, x, y, xSize, ySize):
        self.xCord = x
        self.yCord = y
        self.xSize = xSize
        self.ySize = ySize
        self.surface = pygame.Surface((xSize, ySize))
        
    def createSurface(self, win):
        self.surface.set_alpha(120)
        self.surface.fill(255, 255, 255)
        win.blit(self.surface, (self.xCord, self.yCord))
        


