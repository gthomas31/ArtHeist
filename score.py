import pygame
pygame.init()

class ScoreCounter:

    def __init__(self, counter, f):
        self.currentScore = counter
        self.fails = f

    def score(self, screen, counter):
        white = (255,255,255)
        score_font = pygame.font.SysFont('Comic Sans MS', 24, bold = True, italic=True)
        Score_Line = "Paintings Stolen:  " + str(self.currentScore)
        Fails_Line =  "Attempts: " + str(self.fails)
        Score_display = score_font.render(Score_Line, 2, white)
        Fails_display = score_font.render(Fails_Line, 2, white)
        screen.blit(Score_display, (950,10))
        screen.blit(Fails_display, (950, 37))

        

    #return (score)