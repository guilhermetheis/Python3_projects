'''
This is a python based snake game to learn how to use pygame and for some fun during my trips by bus (student life in Europe rules man)
Based on: https://pythonspot.com/snake-with-pygame/
Date: 29/03/2019
Version: 0.0.1
Author: Guilherme Theis
License: MIT
'''

stringVersion = "v0.0.1"

# Imports
import os
from pygame.locals import *
import pygame

class Player: #creating the player
    x = 10 # initial X position
    y = 10 # initial Y position
    speed = 1 # speed

    # Methods
    #easy to understand directions
    def moveRight(self):
        self.x = self.x + self.speed
    def moveLeft(self):
        self.x = self.x - self.speed
    def moveUp(self):
        self.x = self.x + self.speed
    def moveDown(self):
        self.x = self.y - self.speed

class GameWindow:

    # simple 800x600 window
    windowWidth = 800
    windowHeight = 600

    player = 0

    def __init__(self): #init of the clas
        pygame.init
        self._running = True #private
        self._display_surf = None
        self._image_surf = None
        self.player = Player()

    def on_init(self):
        pygame.init
        self_display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight)) # creating display
        pygame.display.set_caption('PySnake '+stringVersion)
        self._running = True
        self._image_surf = pygame.image.load("pygame.png").convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
    
    def on_loop(self):
        pass
    
    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        self._display_surf.blit(self._image_surf, (self.player.x, self.player.y), pygame.HWSURFACE)
        pygame.display.flip

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed() 
 
            if (keys[pygame.K_RIGHT]):
                self.player.moveRight()
 
            if (keys[pygame.K_LEFT]):
                self.player.moveLeft()
 
            if (keys[pygame.K_UP]):
                self.player.moveUp()
 
            if (keys[pygame.K_DOWN]):
                self.player.moveDown()
 
            if (keys[K_ESCAPE]):
                self._running = False
 
        self.on_loop()
        self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theWindow = GameWindow()
    theWindow.on_execute()
    