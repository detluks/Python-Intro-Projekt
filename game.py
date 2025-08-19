import pygame 


pygame.init
width, height = 500,750
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spaceshooter")
player=[]
for i in range(3):
    img= pygame.image.load(f"images/ship_{i}.png")
    player.append(img)
speed = 8
x,y=width/2,height*(2/3)
clock = pygame.time.Clock()
frame=0
running = True
w_pressed=False
s_pressed=False
a_pressed=False
d_pressed=False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            elif event.key == pygame.K_w:
                w_pressed = True

            elif event.key == pygame.K_s:
                s_pressed = True

            elif event.key == pygame.K_d:
                d_pressed = True

            elif event.key == pygame.K_a:
                a_pressed = True
            elif event.key == pygame.K_SPACE:
                projectile_fired = True

        
        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_w:
                w_pressed = False 
            elif event.key == pygame.K_s:
                s_pressed = False 
            elif event.key == pygame.K_d:
                d_pressed = False 
            elif event.key == pygame.K_a:
                a_pressed = False 

    if w_pressed:
        y-=speed
    if s_pressed:
        y+=speed
    if d_pressed:
        x+=speed
    if a_pressed:
        x-=speed
    



    screen.fill((100,100,100))
    r=int(frame/4)%3
    screen.blit(player[r],(x,y))
    pygame.display.flip()
    clock.tick(60)
    frame+=1
    

pygame.quit()
