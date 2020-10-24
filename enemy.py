import pygame

class Enemy:

    # Initialize enemy
    def __init__(self, enemyImg):
        self.enemyImg = enemyImg
        self.enemyPic = pygame.image.load(enemyImg)
        self.enemyX = 400
        self.enemyY = 400
        self.enemyX_change = 0.5
        self.enemyY_change = 0

    # Player definition
    def enemy(self, x, y, screen):
        screen.blit(self.enemyPic, (x, y))

    def boundaries(self, screen):
        self.enemyX += self.enemyX_change

        if enemyX <= 700:
            enemyX = 700
        elif enemyX >= 1100:
            enemyX = 1100

        if enemyY <= 0:
            enemyY = 0
        elif enemyY >= 680:
            enemyY = 680

        self.enemy(self.enemyX, self.enemyY, screen)
        pygame.display.update()

    def movement(self):
        # Enemy movement
        if enemyX == 1100:
            enemyX_change = -0.5
        if enemyX == 700:
            enemyX_change = 0.5
