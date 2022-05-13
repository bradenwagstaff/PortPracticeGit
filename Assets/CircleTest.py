import pygame
import sys
pygame.init()
fps=30
fpsclock=pygame.time.Clock()
sur_obj=pygame.display.set_mode((400,300))
pygame.display.set_caption("Keyboard_Input")
White=(255,255,255)

myX= 10
myY= 10

def update(myX, myY):
    
    step=5
    # while True:
    sur_obj.fill(White)
    pygame.draw.rect(sur_obj, (255,0,0), (myX, myY, 70, 65))
    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    key_input = pygame.key.get_pressed()   
    if key_input[pygame.K_LEFT]:
        myX -= step
    if key_input[pygame.K_UP]:
        myY -= step
    if key_input[pygame.K_RIGHT]:
        myX += step
    if key_input[pygame.K_DOWN]:
        myY += step
    pygame.display.update()
    fpsclock.tick(fps)
        # return [p1, p2]
    # print(f"X: {p1}")

update(myX=10, myY=10)