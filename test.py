import pygame

pygame.init()

win = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Art Heist")
    #INSERT WINDOW LOGO
    #icon = pygame.image.load()
    #pygame.display.set_icon(icon)
s = pygame.Surface((400, 400))
s.set_alpha(100)
s.fill((255,255,255))
win.blit(s, (200, 50))
print(pygame.Surface.get_bounding_rect(s))
pygame.display.update()

#print(x.bottomleft[0])
x, y = pygame.mouse.get_pos()
print(x)
    #run until closed
running = True 
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

pygame.display.update()





