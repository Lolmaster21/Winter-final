import pygame
from settings import *
from level import Level
from Platform import *



class Game:
    def __init__(self):
        pygame.init()
        self.clock =pygame.time.Clock()
        self.level = Level()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            dt= self.clock.tick()/1000
            self.level.run(dt)
            pygame.display.update()
        #end of game loop------------------------------------------
            

#---------- main(starting point of program)-------------------------------------
if __name__=='__main__':
    game = Game()
    game.run()
