import pygame
pygame.init()

class ScoreCounter:

    def __init__(self, counter):
        self.currentScore = counter

    def score(self, screen, counter):
        white = (255,255,255)
        score_font = pygame.font.SysFont('Comic Sans MS', 24, bold = True, italic=True)
        Score_Line = "Paintings Stolen:  " + str(self.currentScore)
        Score_display = score_font.render(Score_Line, 2, white)
        screen.blit(Score_display, (950,10))

        

    #return (score)