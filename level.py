import pygame as py
from settings import *
from tiles import Tile
from player import Player


class Level:
    def __init__(self,level_data,surface):
        #gets a reference (address) to the currently set display surface
        self.display_surface = surface
        self.setup_level(level_data)
        #class "group" is part of pygame's sprites support. it is a class that manages a *list* of sprites.
        self.all_sprites = py.sprite.Group()

        self.setup()#call the setup function

    def setup(self):
        self.player = Player((640, 360), self.all_sprites)

    def setup_level(self,layout):
        self.tiles = py.sprite.Group()
        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                #print(f'{row_index},{col_index}:{cell}')
                if cell == 'x':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)


        

    def run(self, dt):
        #print("run game")
        self.display_surface.fill('black')
        self.tiles.draw(self.display_surface)
        self.all_sprites.draw(self.display_surface)#draw fuction from group class
        self.all_sprites.update(dt)#another fuction from group class

