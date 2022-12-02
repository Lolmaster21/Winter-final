import pygame as py

class Tile(py.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = py.Surface((size,size))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(topleft = pos)
