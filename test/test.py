import pygame



win = pygame.display.set_mode((500,500))

play = True
while play:
    pygame.draw.circle(win, (0,255,255), (200, 300), 100, 3)
    pygame.display.flip()