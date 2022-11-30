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

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
                self.direction.y = -1
                self.direction.x = -1

        if keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
                self.direction.y = 1
                self.direction.x = 1

        if keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
                self.direction.y = 1
                self.direction.x = -1


        elif keys[pygame.K_UP]:
                self.direction.y = -1
                self.status = "up"
        
        elif keys[pygame.K_DOWN]:
                self.direction.y = 1
                self.status = "down"
        
        elif keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.status = "right"

        elif keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.status = "left"

        else:
                self.direction.x = 0
                self.direction.y = 0

        


    def move(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos

    def update(self,dt):
        self.input()
        self.move(dt)
    
