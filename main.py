import sys, pygame
import numpy as np
pygame.init()

size  = width, height = 700, 700
speed = [2, 2]
black = (0,0,0)
red   = (255,0,0)
green = (0,255,0)
blue  = (0,0,255)
white = (255,255,255)

screen = pygame.display.set_mode(size)

for i in range(50,651,200):
    pygame.draw.line(screen, white, (50,i), (650,i), 2)
    pygame.draw.line(screen, white, (i,50), (i,650), 2)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    pygame.draw.circle(screen, "blue", [250, 250], 40, 0, draw_top_right=True)
    pygame.draw.ellipse(screen, "red", [300, 10, 50, 20])

    pygame.display.flip()
 