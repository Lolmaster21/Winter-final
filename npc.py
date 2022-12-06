import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))
WalkLeft = pygame.image.load('Cheebss.jpg')
WalkRight = pygame.image.load('invertedd.jpg')
clock = pygame.time.Clock()

xpos = 400
ypos = 100
direction = 0
fall = 0
isOnGround = False
width = 100
height = 100
vx = 0 #player left/right speed
vy = 0 #player up/down speed
cxpos = 0
cypos = 0
npc = True
#-----------class definitions------------------------------------------
class enemy:
    def __init__(self, cxpos, cypos):
        self.cxpos = cxpos
        self.cypos = cypos
        self.counter = 0
        self.vx = 2
        self.vy = 0
        self.isOnGround = False
       
    def draw(self, npc):
        print("inside draw function")
        if npc == 1:
            if self.vx > 0:
                screen.blit(WalkRight, (self.cxpos, self.cypos))
            if self.vx < 0:
                screen.blit(WalkLeft,(self.cxpos, self.cypos))
               
    def move(self):
        if self.cxpos < 0 or self.cxpos + 100 > 500:
          self.vx *= -1

        self.cxpos += self.vx
        self.cypos += self.vy
   
    def gravity(self, npc):
        if npc == 1:
            if self.cypos > 500 - 100: #check if your feet are on the ground
                self.isOnGround = True
                self.cypos = 500 - 100
                self.vy = 0 #stot falling if on ground
            else:
                self.isOnGround = False
            if self.isOnGround == False:
                self.vy+=.2 #if not on ground, fall downwards  


               
#class definition---------------------------------------------------------------
bruh = enemy(cxpos, cypos)

status = True
while (status): #GAME LOOP
    clock.tick(60)
  # iterate over the list of Event objects
  # that was returned by pygame.event.get() method.
    #INPUT SECTION------------------------------------
 
    for i in pygame.event.get():
 
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if i.type == pygame.QUIT:
            status = False
           
           
       
    #PHYSICS----------------------------------------
   
   

    bruh.move()

   

   
    #RENDER SECTION---------------------------------
    #clear screen
    screen.fill((255, 255, 255))
    #call draw functions here
    bruh.draw(npc)
    #display flip goes here
    pygame.display.flip()
       

pygame.quit()
