import pygame
from settings import *
from level import Level



class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.clock =pygame.time.Clock()
        self.level = Level()
        self.ticker = 0
        self.frameNum = 0

        
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

