import pygame
pygame.init()
screen=pygame.display.set_mode((400,400))
screen.fill((255,255,255))
GREEN=(0,255,0)

#solid cirlce
pygame.draw.circle(screen,GREEN,(300,300),70)

#outline circle
pygame.draw.circle(screen,GREEN,(100,100),70,10)
pygame.display.update()


done=True
while done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=False
pygame.quit()