from game_engine.Sprite import Sprite
from game_engine.RelativeSprite import RelativeSprite
from racetrack import Racetrack
import pygame
from math import sqrt

diagonalMultiplier = 0.0001;

class Car_visual(RelativeSprite):

    def __init__(self,objectDraw,scaleMultiplier=1):
        

        screenXSize = objectDraw.screenSizeX;
        screenYSize = objectDraw.screenSizeY;

        diagonal = sqrt(screenXSize**2 + screenYSize**2);
        scale = scaleMultiplier*diagonal*diagonalMultiplier;

        super(Car_visual,self).__init__("racecar",0,0,scale,"assets/racecar.png",objectDraw);

        self.setZeroRotation(90);

       
        



        