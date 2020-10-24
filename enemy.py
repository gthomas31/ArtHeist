import pygame

class Enemy:

    # Initialize enemy
    def __init__(self, enemyImg, startingX, startingY):
        self.enemyImg = enemyImg
        self.enemyPic = pygame.image.load(enemyImg)
        self.enemyX = startingX
        self.enemyY = startingY
        self.enemyX_change = 0.5
        self.enemyY_change = 0

    # Player definition
    def enemy(self, x, y, screen):
        screen.blit(self.enemyPic, (x, y))

    def boundaries(self, screen):
        self.enemyX += self.enemyX_change

        if self.enemyX <= 700:
            self.enemyX = 700
        elif self.enemyX >= 1100:
            self.enemyX = 1100

        if self.enemyY <= 0:
            self.enemyY = 0
        elif self.enemyY >= 680:
            self.enemyY = 680

        self.enemy(self.enemyX, self.enemyY, screen)
        pygame.display.update()

    def movement(self):

        # Enemy movement
        if self.enemyX == 1100:
            self.enemyX_change = -0.5
        if self.enemyX == 700:
            self.enemyX_change = 0.5
