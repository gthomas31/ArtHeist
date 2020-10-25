
import pygame
pygame.init()

def score(screen, Number):
    
        count = 0
        white = (255,255,255)
        score_font = pygame.font.SysFont('Comic Sans MS', 24, bold = True, italic=True)
        Score_Line = "Paintings Stolen:  "
        painting = pygame.image.load("Painting.png")
        screen.blit(painting, (420,590))
        Score_display = score_font.render(Score_Line, 2, white)
        screen.blit(Score_display, (950,10))

        

    #return (score)
    
    














