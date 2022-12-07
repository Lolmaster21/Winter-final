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

        if player_x < SCREEN_WIDTH / 4  and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > SCREEN_WIDTH - (SCREEN_WIDTH / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def horizontalcollision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0 :
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0 :
                    player.rect.right = sprite.rect.left

    def verticalcollision(self):
        player = self.player.sprite
        player.gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):       
                if player.direction.y < 0 :
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                elif player.direction.y > 0 :
                    player.direction.y = 0
                    player.rect.bottom = sprite.rect.top
    def run(self):

        #print("run game")
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        self.player.update(self.world_shift)
        self.horizontalcollision()
        self.verticalcollision()        
        self.player.draw(self.display_surface)#draw fuction from group class
        
