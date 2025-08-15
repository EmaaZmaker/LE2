import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("color changin sprite :o")
red=pygame.Color('red')
green=pygame.Color('green')
yellow=pygame.Color('yellow')
blue=pygame.Color('blue')
white=pygame.Color('white')
current_color=white
clock=pygame.time.Clock()
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        x=x-3
    if pressed[pygame.K_RIGHT]:
        x=x+3
    if pressed[pygame.K_UP]:
        y=y-3
    if pressed[pygame.K_DOWN]:
        y=y+3
    x=min(max(0,30),440)
    y=min(max(0,30),440)
    if x==0:
        current_color=blue
    elif x==440:
        current_color=yellow
    elif y==0:
        current_color=red
    elif y==440:
        current_color=green
    else:
        current_color=white
    screen.fill((0,0,0))
    pygame.draw.rect(screen,current_color,(x,y,60,60))
    pygame.display.flip()
    clock.tick(90)
pygame.quit()