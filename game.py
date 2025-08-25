import pygame 
import random


pygame.init()
pygame.mixer.init()
width, height = 500,750
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spaceshooter")
player=[]
alienImg=[]
for i in range(3):
    img= pygame.image.load(f"images/ship_{i}.png")
    player.append(img)
for i in range(2):
    img = pygame.image.load(f"images/alien_{i}.png")
    alienImg.append(img)
bulletSound = pygame.mixer.Sound("sounds/laser.mp3")
speed = 8
bulletSpeed=10
bullets=[]
aliens=[]
framesTimer=0
alienSpeed=6
bulletFired=False
x,y=width/2,height*(2/3)
player_width=player[0].get_rect().size[0]
alien_width=alienImg[0].get_rect().size[0]
alien_Height=alienImg[0].get_rect().size[1]
clock = pygame.time.Clock()
frame=0
a = 0
running = True
w_pressed=False
s_pressed=False
a_pressed=False
d_pressed=False


class Bullet:
    def __init__(self,x,y,speed):
        self.x=x
        self.y=y
        self.speed=speed
    def move(self):
        self.y-=self.speed
    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 5, 10))

class Alien:
    def __init__(self,x,y,speed):
        self.x=x
        self.y=y
        self.speed=speed
    def move(self):
        self.y+=self.speed
    def draw(self):
        screen.blit(alienImg[a],(self.x,self.y))

    
while running:
    screen.fill((100,100,100))
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
                bulletFired = True

        
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
    if bulletFired:
        bulletSound.play()
        bullets.append(Bullet(x+player_width/2,y,bulletSpeed))
        bulletFired=False

    for element in bullets:
        element.move()
        element.draw()
        if element.y<=0:
            bullets.remove(element)
        
    if framesTimer>200:
        aliens.append(Alien(random.randint(0,width-alien_width),0,alienSpeed))
        framesTimer = 0
    a=int(frame/4)%2
    for element in aliens:
        element.move()
        element.draw()



  
    r=int(frame/4)%3
    screen.blit(player[r],(x,y))
    pygame.display.flip()
    clock.tick(60)
    frame+=1
    framesTimer+=1
    

pygame.quit()
