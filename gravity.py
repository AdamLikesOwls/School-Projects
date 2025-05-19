import pygame 

# Pygame Initialisation
pygame.init()

# Clock for FPS
clock = pygame.time.Clock()

#
white = (255,255,255)
# Screen Properties
width, height = 1200,800
screen = pygame.display.set_mode((width,height))

# Rectangle Properties
x,y = 100,100
rectx,recty = 40,40

# Movement Variables
gravity = 0.1
acl = 0.02
speed = 0.5

vel_x = 0
vel_y = 0 


# Platform Classes

def draw(posx,posy,sizex,sizey):
       platform = pygame.draw.rect(screen,white,[posx,posy,sizex,sizey],30)
    
# GameLoop
running = True

while running:


    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # Bottom screen Collision
    if y > (height-recty):
        vel_y = 0
        y = height-recty
    
    if  x > (width-rectx):
        x = width - rectx
        vel_x = 0

    if  x < (0):
        x = 0
        vel_x = 0
    
        


    # Key Inputs
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if y == (height-recty):
            vel_y -= 10

    if keys[pygame.K_a]:
         vel_x += speed
         x += vel_x * -acl


    if keys[pygame.K_d]:
        vel_x += speed
        x += vel_x * acl
    

    
    # Gravity
    vel_y += gravity 
    y += vel_y * 0.5


    # Player and Objects
    rect = pygame.draw.rect(screen, (255,255,255),[x,y,rectx,recty], 30)

    # Platforms
    platform1 = draw(600,600,500,40)

    # Screen Update

    pygame.display.update()
    pygame.display.flip()
    clock.tick()

pygame.quit()
