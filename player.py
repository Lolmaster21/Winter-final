import pygame 
from settings import *

class Player(pygame.sprite.Sprite):

    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((32,64))
        self.image.fill('blue')
        self.rect = self.image.get_rect(topleft = pos)

        self.isOnGround = False
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
      
    def gravity(self):
        if self.rect.y > len(LEVEL_ONE * tile_size)-32:
            self.isOnGround = True
            self.rect.y = len(LEVEL_ONE * tile_size)-64 #Position
        else: 
            self.isOnGround = False

        if self.isOnGround == False: #Gravity function 
            self.direction.y += .2
         
        self.rect.y += self.direction.y 

    def input(self):
           keys = pygame.key.get_pressed()
           if keys[pygame.K_SPACE] == True and self.isOnGround == True:
               self.direction.y = -1 
               
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

    def update(self):
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y 
        self.input()
        self.gravity()
