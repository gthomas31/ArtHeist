import pygame, player, score

class Enemy:

    # Initialize enemy
    def __init__(self, enemyImg, startingX, startingY, leftBound, rightBound, scores):
        self.enemyImg = enemyImg
        self.enemyPic = pygame.image.load(enemyImg)
        self.enemyX = startingX
        self.enemyY = startingY
        self.enemyX_change = 0.5
        self.enemyY_change = 0
        self.xenemyboxsize = 55
        self.yenemyboxsize = 95
        self.leftBoundary = leftBound
        self.rightBoundary = rightBound
        self.enemybox = pygame.Surface((self.xenemyboxsize, self.yenemyboxsize))
        self.alive = True
        self.scores = scores

    # Player definition
    def enemy(self, x, y, screen):
        screen.blit(self.enemyPic, (x, y))
        self.enemybox.set_alpha(0)
        self.enemybox.fill((0, 0, 100))
        screen.blit(self.enemybox, (x + 3, y + 20))
    
    def kill(self):
        self.alive = False

    def boundaries(self, screen):
        self.enemyX += self.enemyX_change

        if self.enemyX <= self.leftBoundary:
            self.enemyX = self.leftBoundary
        elif self.enemyX >= self.rightBoundary:
            self.enemyX = self.rightBoundary

        if self.enemyY <= 0:
            self.enemyY = 0
        elif self.enemyY >= 680:
            self.enemyY = 680

        self.enemy(self.enemyX, self.enemyY, screen)

    def movement(self, player):

        # Enemy movement
        if self.enemyX == self.rightBoundary:
            self.enemyX_change = -0.5
        if self.enemyX == self.leftBoundary:
            self.enemyX_change = 0.5
        self.collision(player)
    
    def collision(self, player):
        if (self.alive):
            #player values------------------------

            #top left values
            pxhitbox = player.playerX + 5
            pyhitbox = player.playerY + 20

            #size
            pxhitboxsize = player.xboxsize
            pyhitboxsize = player.yboxsize

            #bottom right values
            pnewx = pxhitbox + pxhitboxsize
            pnewy = pyhitbox + pyhitboxsize


            #enemy values --------------------------

            #top left values
            exhitbox = self.enemyX + 3
            eyhitbox = self.enemyY + 20

            #size
            exhitboxsize = self.xenemyboxsize
            eyhitboxsize = self.yenemyboxsize

            #bottom right values 
            enewx = exhitboxsize + exhitbox
            enewy = eyhitbox + eyhitboxsize

            if (exhitbox < pxhitbox < enewx) and (eyhitbox < pyhitbox < enewy): 
            #if (player.playerX + 50 < self.enemyX < player.playerX + 100): 
                player.playerX = 100
                player.playerY = 600
                self.scores.fails += 1
                
            elif (exhitbox < pnewx < enewx) and (eyhitbox < pyhitbox < enewy):
                player.playerX = 100
                player.playerY = 600
                self.scores.fails += 1
            elif (exhitbox < pnewx < enewx) and (eyhitbox < pnewy < enewy):
                player.playerX = 100
                player.playerY = 600
                self.scores.fails += 1
            elif (exhitbox < pxhitbox < enewx) and (eyhitbox < pnewy < enewy): 
                player.playerX = 100
                player.playerY = 600
                self.scores.fails += 1
        


        

    
    #player top left corner check enemy top right
    #player top right corner check enemy top left
    #player bottom left check enemy top left]
    #player bottom right check enemy top right
    #----------------------------------------------------
    #player midpoint of left side check enemy top right
    #player midpoint of right check enemy top left 
    #

    #y value of the top left and x value of bottom right = top right