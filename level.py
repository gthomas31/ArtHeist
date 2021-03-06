import pygame

class Level:

    def __init__(self, imgFile, groundLevel):
        self.background = imgFile
        self.backgroundImage = pygame.image.load(self.background)
        self.groundLevel = groundLevel
        self.platformList = []
        self.paintingList = []

    def displayBackground(self, win):
        win.blit(self.backgroundImage, (0, 0))
        for platform in self.platformList:
           platform.createSurface(win)
        for painting in self.paintingList:
            painting.createPainting(win)

    def changeBackgroundImage(self, img, screen):
        self.backgroundImage = pygame.image.load(img)
        screen.blit(self.backgroundImage, (0,0))

    def addPlatform(self, platform, win):
        # win.blit(platform.surface, (platform.xCord, platform.yCord))
        self.platformList.append(platform)

    def clearScreen(self, win):
        self.backgroundImage = pygame.image.load('WhiteScreen.png')
        self.displayBackground(win)

    def addPainting(self, painting, win):
        self.paintingList.append(painting)

    def removePlatforms(self):
        self.platformList = []

    def removePaintings(self):
        self.paintingList = []

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
        self.surface.set_alpha(0) # make 0 for invisible
        self.surface.fill((255, 255, 255))
        self.displaySurface(win)

    def displaySurface(self, win):
        win.blit(self.surface, (self.xCord, self.yCord))
        
class Level2(Level):

    def __init__(self, groundLevel):
        super().__init__('LevelTwo.png', groundLevel)

