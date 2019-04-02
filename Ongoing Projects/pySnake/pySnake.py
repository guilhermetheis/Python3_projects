'''
This is a python based snake game to learn how to use pygame and for some fun during my trips by bus (student life in Europe rules man)
Based on: https://pythonspot.com/snake-with-pygame/
'''
__date__ = "29/03/2019"
__author__ = "Guilherme Theis"
__copyright__ = "Copyright 2019, GTheis"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Guilherme Theis"
__email__ = "Guilherme Theis"
__status__ = "Development"


# Imports
import sys
import os
from pygame.locals import *
import pygame
import time
import random

# Colors!

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

class Apple:
    def __init__(self):
        self.appleFlag = False
    def draw(self,surface , snakeXPos, snakeYPos):#draw.rect method needs a surface that is created in the GameWindow later on.
        #Try...Except used to not coincide with the snake
        if self.appleFlag == False: #if there is not an apple in the map

            try:
                self.ypos = random.randrange(0, 590, 10)
            except self.ypos != snakeYPos:
                pass
            try:
                self.xpos = random.randrange(0, 790, 10)
            except self.xpos != snakeXPos:
                pass
            pygame.draw.rect(surface, red, (self.ypos, self.ypos, 10, 10))
            self.appleFlag = True
        else:
            pygame.draw.rect(surface, red, (self.ypos, self.ypos, 10, 10))
        
class Snake: # creating the snake (array of x by y pixels)

    def __init__(self): #constructor
        self.ypos = 300 #Initial Y pos
        self.xpos = 400 #Initial X pos
        self.distance = 10 #How many pixels the snakes move per period (each apple will be 10x10 so I have 80x60 squares)

    def moveRight(self):
        self.xpos = self.xpos + self.distance #moving
    def moveLeft(self):
        self.xpos = self.xpos - self.distance
    def moveUp(self):
        self.ypos = self.ypos - self.distance
    def moveDown(self):
        self.ypos = self.ypos + self.distance

    def draw(self, surface): #draw.rect method needs a surface that is created in the GameWindow later on.
        pygame.draw.rect(surface, green, (self.xpos, self.ypos, 10, 10))
        


    #def update(self): #update method to renew position and size each period
        #if self.

class GameWindow:

    windowWidth = 800
    windowHeight = 600
    difficulty = 10 #this divides the render time of the game this making it faster or slower.
 
    def __init__(self): #Constructor
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.snake = Snake() #Creating snake mathod
        self.apple = Apple() #creating apple
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        pygame.display.set_caption('pySnake '+ __version__)
        self._running = True
 
    def on_event(self, event): #quit
        if event.type == quit:
            self._running = False
 
    def on_loop(self):
        pass
 
    def on_render(self):
        self._display_surf.fill((0,0,0)) #Color of the board
        self.snake.draw(self._display_surf) #draw snake
        self.apple.draw(self._display_surf, self.snake.xpos, self.snake.ypos) #draw apple
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
            pygame.time.delay(int(500/self.difficulty)) #delay to renew the render (ms)
        self.on_cleanup()

def main():
    theWindow = GameWindow()
    theWindow.on_execute()

if __name__ == "__main__":
    main()