import pygame, level

class Player:

    # Initialize player
    def __init__(self, playerImg):
        self.playerImg = playerImg
        self.playerPic = pygame.image.load(playerImg)
        self.playerX = 600
        self.playerY = 400
        self.playerX_change = 0
        self.playerY_change = 0
        self.playerHeight = 120
        self.currentGroundLevel = 0

    def changeImageFile(self, playerImg):
        self.playerImg = playerImg
        self.playerPic = pygame.image.load(playerImg)

    # Player definition
    def player(self, x, y, screen):
        screen.blit(self.playerPic, (x, y))

    def boundaries(self, screen, level):
        self.playerX += self.playerX_change     
        self.gravity(self.currentGroundLevel)
        self.currentGroundLevel = level.groundLevel
        self.playerY += self.playerY_change

        if self.playerX <= 0:
            self.playerX = 0
        elif self.playerX >= 1140:
            self.playerX = 1140

        if self.playerY <= 0:
            self.playerY = 0
        elif self.playerY >= 680:
            self.playerY = 680
        
        for index in range(len(level.platformList)):
            x1, x2, y1 = level.findTop(index)
            x1, x2, y2 = level.findBottom(index)
            if (self.playerY + 90 > y1 and self.playerY + 90 < y2):
                if (x1 < self.playerX + 30 < x2):
                    self.playerY = y1 - 90
                    self.currentGroundLevel = y1
                    self.playerY_change = 0
            x1, y1, y2 = level.findLeftSide(index)
            x2, y1, y2 = level.findRightSide(index)
            side = "right"
            if (self.playerX <= x1):
                side = "left"
            else:
                side = "right"
            if (self.playerX > x1 - 50 and self.playerX < x2):
                if (y2 < self.playerY + 90 and y1 > self.playerY - 90):
                    if (side == "right"):
                        self.playerX = x2
                    else:
                        self.playerX = x1 - 50
                    self.playerX_change = 0

        self.player(self.playerX, self.playerY, screen)
        # pygame.display.update()

    # Keystroke functions
    def movement(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.playerX_change = -2
                print("Left arrow")
            if event.key == pygame.K_RIGHT:
                self.playerX_change = 2
                print("Right arrow")
            if event.key == pygame.K_SPACE:
                print("Space")
                print(self.playerY_change)
                if self.playerY_change == 0:
                    self.playerY_change = -2.5
                    print("Up arrow")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.playerX_change = 0
                print("Released")

    def gravity(self, groundLevel):
        if self.playerY_change == 0:
            self.playerY_change = 1
        else:
            self.playerY_change += .025

        if self.playerY >= groundLevel - self.playerHeight and self.playerY_change > 0:
            self.playerY_change = 0
            