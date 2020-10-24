import pygame

class Level:
    
    platformList = []

    def __init__(self, imgFile, groundLevel):
        self.background = imgFile
        self.backgroundImage = pygame.image.load(self.background)
        self.groundLevel = groundLevel

    def displayBackground(self, win):
        win.blit(self.backgroundImage, (0, 0))
        for platform in self.platformList:
           platform.createSurface(win)

    def addPlatform(self, platform, win):
        win.blit(platform.surface, (platform.xCord, platform.yCord))
        self.platformList.append(platform)

    def removePlatforms(self):
        self.platformList = []

    def findTop(self, index):
        # x1, x2, y
        x1 = self.platformList[index].xCord
        y = self.platformList[index].yCord
        x2 = x1 + self.platformList[index].xSize
        return x1, x2, y
    
    def findBottom(self, index):
        # x1, x2, y
        x1, x2, y = self.findTop(index)
        y += self.platformList[index].ySize
        return x1, x2, y
    
    def findLeftSide(self, index):
        # x, y1, y2
        x = self.platformList[index].xCord
        y1 = self.platformList[index].yCord
        y2 = y1 + self.platformList[index].ySize
        return x, y1, y2
    
    def findRightSide(self, index):
        # x, y1, y2
        x, y1, y2 = self.findLeftSide(index)
        x += self.platformList[index].xSize
        return x, y1, y2


class Platform:

    def __init__(self, x, y, xSize, ySize):
        self.xCord = x
        self.yCord = y
        self.xSize = xSize
        self.ySize = ySize
        self.surface = pygame.Surface((xSize, ySize))
        
        
    def createSurface(self, win):
        self.surface.set_alpha(120) # make 0 for invisible
        self.surface.fill((255, 255, 255))
        self.displaySurface(win)

    def displaySurface(self, win):
        win.blit(self.surface, (self.xCord, self.yCord))
        


