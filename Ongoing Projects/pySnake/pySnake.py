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

class GameWindow:

    windowWidth = 800
    windowHeight = 600
 
    def __init__(self): #Constructor
        self._running = True
        self._display_surf = None
        self._image_surf = None
 
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
        self._display_surf.fill((0,0,0))
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
        sys.exit()
 
    def on_execute(self):

        if self.on_init() == False:
            self._running = False

        while(self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed() 
 
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