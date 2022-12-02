import pygame as py
from settings import *
from tiles import Tile
from player import Player


class Level:
    def __init__(self,level_data,surface):
        #level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
         
    def setup_level(self,layout):
        self.tiles = py.sprite.Group()
        self.player = py.sprite.GroupSingle()

        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                #print(f'{row_index},{col_index}:{cell}')
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'x':
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'p':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < 200 :
            self.world_shift = 8
            player.speed = 0
        elif player_x >1000:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player = 8

    def run(self):

        #print("run game")
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        self.player.update()
        self.player.draw(self.display_surface)#draw fuction from group class
        self.scroll_x()

