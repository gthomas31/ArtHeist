import pygame
pygame.init()

class Painting:

    def __init__(self, img, x, y, screen):
        self.image = img
        self.imagePic = pygame.image.load(img)
        self.xSize = 46
        self.ySize = 41
        self.left = x
        self.top = y
        self.right = self.left + self.xSize
        self.bottom = self.top + self.ySize 
        self.surface = pygame.Surface((self.xSize, self.ySize))
        self.surface.set_alpha(100)
        self.surface.fill((0, 0, 100))
        screen.blit(self.surface, (self.left, self.top))

    def createPainting(self, win):
        self.surface.set_alpha(0) # make 0 for invisible
        self.surface.fill((255, 255, 255))
        self.displaySurface(win)

    def displaySurface(self, win):
        win.blit(self.surface, (self.left, self.top))
        win.blit(self.imagePic, (self.left, self.top))

    def collision(self, player):
       #top left values
        pxhitbox = player.playerX + 5
        pyhitbox = player.playerY + 20

        #size
        pxhitboxsize = player.xboxsize
        pyhitboxsize = player.yboxsize

        #bottom right values
        pnewx = pxhitbox + pxhitboxsize
        pnewy = pyhitbox + pyhitboxsize

        if (pxhitbox < self.left < pnewx) and (pyhitbox < self.top < pnewy): 
            player.playerX = 100
            player.playerY = 600
            return True
        if (pxhitbox < self.left < pnewx) and (pyhitbox < self.bottom < pnewy):
            player.playerX = 100
            player.playerY = 600
            return True
        if (pxhitbox < self.right < pnewx) and (pyhitbox < self.top < pnewy):
            player.playerX = 100
            player.playerY = 600
            return True
        if (pxhitbox < self.right < pnewx) and (pyhitbox < self.bottom < pnewy): 
            player.playerX = 100
            player.playerY = 600
            return True