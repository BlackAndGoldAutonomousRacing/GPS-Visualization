from game_engine.Sprite import Sprite
import pygame
from math import sqrt

diagonalMultiplier = 0.00001;

class Car_visual(Sprite):

    def __init__(self,objectDraw):
        

        screenXSize = objectDraw.screenSizeX;
        screenYSize = objectDraw.screenSizeY;

        diagonal = sqrt(screenXSize**2 + screenYSize**2);
        scale = diagonal*diagonalMultiplier;

        super(Car_visual,self).__init__("racecar",100,100,0.1,"assets/racecar.png");


        
        # add this object to the object draw to be rendered and updated
        objectDraw.add(self);
        # init stuff

    def recieveGpsPos(self,x,y):
        self.setPosition(x,y);

    def update(self):
        #print(self.xPosition,self.yPosition);
        return super().update()
