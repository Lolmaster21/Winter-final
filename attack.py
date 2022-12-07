import pygame as py
from settings import *

class Attack():
    def __init__(self,a,b,c):
        super().__init__()
        self.atkx = a
        self.atky = b
        self.direc = c


    def attack(self,atkx, atky, direc):
        if self.direc  > 0:
            self.atkx += 30
        if self.direc  <=0 :
         self.atkx -= 30
        #py.draw.rect(screen, (5, 250, 50), (atkX, atkY, 20, 20))
        print("attacking at ", self.atkx," , " , self.atky)
