import pygame 


pygame.init()
pygame.mixer.init()
width, height = 500,750
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spaceshooter")
player=[]
for i in range(3):
    img= pygame.image.load(f"images/ship_{i}.png")
    player.append(img)
bulletSound = pygame.mixer.Sound("sounds/laser.mp3")
speed = 8
bulletSpeed=10
bullets=[]
bulletFired=False
x,y=width/2,height*(2/3)
player_width=player[0].get_rect().size[0]
clock = pygame.time.Clock()
frame=0
running = True
w_pressed=False
s_pressed=False
a_pressed=False
d_pressed=False
class bullet:
    def __init__(self,x,y,speed):
        self.x=x
        self.y=y
        self.speed=speed
    def move(self):
        self.y-=self.speed
    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 5, 10))

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
        bullets.append(bullet(x+player_width/2,y,bulletSpeed))
        bulletFired=False

    for element in bullets:
        element.move()
        element.draw()
        

    



  
    r=int(frame/4)%3
    screen.blit(player[r],(x,y))
    pygame.display.flip()
    clock.tick(60)
    frame+=1
    

pygame.quit()
