import pygame
from pygame.locals import *
import sys
 
pygame.init()
display = pygame.display.set_mode((300, 300))
 
x = 0
y = 0
z = 0
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x += -1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                y += -1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SLASH:
                z += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PERIOD:
                z += -1

    print(f"X: {x}")
    print(f"Y: {y}")
    print(f"Z: {z}")
    print("")
        