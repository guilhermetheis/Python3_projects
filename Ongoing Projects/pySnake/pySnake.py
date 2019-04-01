'''
This is a python based snake game to learn how to use pygame and for some fun during my trips by bus (student life in Europe rules man)
Based on: https://pythonspot.com/snake-with-pygame/
'''
__date__ = "29/03/2019"
__author__ = "Guilherme Theis"
__copyright__ = "Copyright 2019, GTheis"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Guilherme Theis"
__email__ = "Guilherme Theis"
__status__ = "Development"


# Imports
import sys
import os
from pygame.locals import *
import pygame
import time

class Snake: # creating the snake (array of x by y pixels)

    def __init__(self): #constructor
        self.ypos = 300 #Initial Y pos
        self.xpos = 400 #Initial X pos
        self.distance = 10 #How many pixels the snakes move per period (each apple will be 10x10 so I have 80x60 squares)

    def moveRight(self):
        self.xpos = self.xpos + self.distance
    def moveLeft(self):
        self.xpos = self.xpos - self.distance
    def moveUp(self):
        self.ypos = self.ypos - self.distance
    def moveDown(self):
        self.ypos = self.ypos + self.distance

    def draw(self, surface): #draw.rect method needs a surface that is created in the GameWindow later on.
        pygame.draw.rect(surface, (0, 255, 0), (self.xpos, self.ypos, 10, 10))
        


    #def update(self): #update method to renew position and size each period
        #if self.

class GameWindow:

    windowWidth = 800
    windowHeight = 600
 
    def __init__(self): #Constructor
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.snake = Snake()
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
 
        pygame.display.set_caption('pySnake '+ __version__)
        self._running = True
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        pass
 
    def on_render(self):
        self._display_surf.fill((0,0,0)) #Color of the board
        self.snake.draw(self._display_surf)
        pygame.display.flip() #update the display of the screen
 
    def on_cleanup(self):
        pygame.quit()
        sys.exit()
 
    def on_execute(self):

        if self.on_init() == False:
            self._running = False

        
        while(self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed() 
 
            if (keys[K_RIGHT]):
                self.snake.moveRight()
 
            if (keys[K_LEFT]):
                self.snake.moveLeft()
 
            if (keys[K_UP]):
                self.snake.moveUp()
 
            if (keys[K_DOWN]):
                self.snake.moveDown()
 
            if (keys[K_ESCAPE]):
                self._running = False
 
            self.on_loop()
            self.on_render()
            time.sleep (50.0 / 1000.0);
        self.on_cleanup()

def main():
    theWindow = GameWindow()
    theWindow.on_execute()

if __name__ == "__main__":
    main()