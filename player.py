import pygame 
from attack import Attack
from settings import *
from mouse import Mouse
class Player(pygame.sprite.Sprite):

    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((32,64))
        self.image.fill('blue')
        self.rect = self.image.get_rect(topleft = pos)
        self.isOnGround = False
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.mouse = Mouse()
        self.click = self.mouse.click
        self.mouse_pos = self.mouse.mouse_pos
        self.start = start
        
    def gravity(self):
        #Gravity function 
        self.direction.y += .8
         
        self.rect.y += self.direction.y 

    def input(self):
        
        while self.start == True:
            for event in pygame.event.get():
                self.mouse.handler(event)
                self.mouse_pos = self.mouse.mouse_pos
                self.click = self.mouse.click
            if self.click == True:
                print("click")
                Attack(self.rect.x,self.rect.y,self.direction.x)
                

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] == True:
            self.jump()
            self.isOnGround = False
        elif keys[pygame.K_d]:
            self.direction.x = -1
        elif keys[pygame.K_a]:
            self.direction.x = 1
        else:
            self.direction.x = 0
                
    def jump(self):
        self.direction.y = -16
    def update(self, amount):
        self.input()
