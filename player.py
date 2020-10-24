import pygame

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

    # Player definition
    def player(self, x, y, screen):
        screen.blit(self.playerPic, (x, y))

    def boundaries(self, screen, groundLevel):
        self.playerX += self.playerX_change      
        self.gravity(groundLevel)
        self.playerY += self.playerY_change

        if self.playerX <= 0:
            self.playerX = 0
        elif self.playerX >= 1140:
            self.playerX = 1140

        if self.playerY <= 0:
            self.playerY = 0
        elif self.playerY >= 680:
            self.playerY = 680
        
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
            