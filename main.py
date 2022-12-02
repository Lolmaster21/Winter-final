import pygame as py
from settings import *
from level import Level
from mouse import Mouse
import sys

#Class-Game-------------------------------------
class Game():
    def __init__(self):
        py.init()
        self.screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HIEGHT))
        self.clock = py.time.Clock()
        self.level = Level(LEVEL_ONE,self.screen)
        self.start = False

        #mouse
        self.mouse = Mouse()
        self.click = self.mouse.click
        self.mouse_pos = self.mouse.mouse_pos

    def Start(self):
        
        while self.start == False:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    sys.exit()

                #mouse
                self.mouse.handler(event)
                self.mouse_pos = self.mouse.mouse_pos
                self.click = self.mouse.click

            #Start
            py.draw.rect(self.screen,(255,255,255),(SCREEN_WIDTH/2-50,400,100,50))
            if ((self.mouse_pos[0] > (SCREEN_WIDTH/2)-50 and self.mouse_pos[0] < (SCREEN_WIDTH/2-50)+100 and
                (self.mouse_pos[1]) > 400 and self.mouse_pos[1] < 450) and self.click == True ):
                self.start = True
            #Settings
            py.draw.rect(self.screen,(255,255,255),(SCREEN_WIDTH/2-50,500,100,50))
            if ((self.mouse_pos[0] > (SCREEN_WIDTH/2)-50 and self.mouse_pos[0] < (SCREEN_WIDTH/2-50)+100 and
                (self.mouse_pos[1]) > 500 and self.mouse_pos[1] < 550) and self.click == True ):
                pass
            #Quit
            py.draw.rect(self.screen,(255,255,255),(SCREEN_WIDTH/2-50,600,100,50))
            if ((self.mouse_pos[0] > (SCREEN_WIDTH/2)-50 and self.mouse_pos[0] < (SCREEN_WIDTH/2-50)+100 and
                (self.mouse_pos[1]) > 600 and self.mouse_pos[1] < 650) and self.click == True ):
                py.quit()
                sys.exit()
            py.display.update()
        #starts the game using run function
        while self.start == True:
            g.run()

    def run(self):
        while True: #GAME-LOOP---------------------------------------
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    sys.exit()

            self.screen.fill('black')
            self.level.run()
            py.display.update()#WORKS LIKE FLIP BUT CAN UPDAT PORTIONS OF THE SCREEN IF WE WANT
            self.clock.tick(60)
            #END-OF-GAME-LOOP--------------------------------------------------------------------------
if __name__ == '__main__':
    g = Game()
    g.Start()#RUNS THE GAME LOOP

