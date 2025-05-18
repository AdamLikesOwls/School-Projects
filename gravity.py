import pygame 

pygame.init()

clock = pygame.time.Clock()

width, height = 900,800
screen = pygame.display.set_mode((width,height))

x,y = 100,100

gravity = 0.1
vel = 0 

running = True

while running:


    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    vel += gravity 
    y += vel * 0.5

    rect = pygame.draw.rect(screen, (255,255,255),[x,y,40,40], 30)

    key = pygame.KEYDOWN
    
    if key: 
        vel -= 50
    
    if y > (height-40):
        vel = 0
        y = height-40





    pygame.display.update()
    pygame.display.flip()
    clock.tick(120)

pygame.quit()
