import pygame
from settings import *

class Player(pygame.sprite.Sprite):

    def __init__(self,pos,group):
        super().__init__(group)
        self.image = pygame.Surface((32,64))
        self.image.fill('blue')
        self.rect = self.image.get_rect(center = pos)

        self.isOnGround = False
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200
      

    def gravity(self):
        if self.pos.y > 720-32:
            self.isOnGround = True
            self.pos.y = 720-32 #Position
        else: 
            self.isOnGround = False

        if self.isOnGround == False: #Gravity function 
            self.direction.y += .2
     
 
     

        self.pos.y +=self.direction.y
        

    def input(self):
           keys = pygame.key.get_pressed()

         
           if keys[pygame.K_SPACE] == True and self.isOnGround == True:
               self.direction.y = -50 
               self.isOnGround = False


           elif keys[pygame.K_d]:
                self.direction.x = 1
                self.direction.y = 0

        
           elif keys[pygame.K_a]:
                self.direction.x = -1
                self.direction.y = 0

               

           else:
                self.direction.x = 0
                self.direction.y = 0



    def move(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos

    def update(self,dt):
        self.input()
        self.move(dt)
        self.gravity()
