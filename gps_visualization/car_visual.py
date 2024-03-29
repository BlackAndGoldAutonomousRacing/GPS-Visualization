from .game_engine.Sprite import Sprite
from .game_engine.RelativeSprite import RelativeSprite
from .racetrack import Racetrack
import pygame
from math import sqrt
import os
from ament_index_python.packages import get_package_share_directory


diagonalMultiplier = 0.0001;

car_images = ["assets/racecar.png","assets/red_arrow.png","assets/blackandgoldcar.png"];
img_rotations = [90,-90,90];
img_scale_factors = [1,0.5,1];

class Car_visual(RelativeSprite):

    def __init__(self,objectDraw,scaleMultiplier=1):


        screenXSize = objectDraw.screenSizeX;
        screenYSize = objectDraw.screenSizeY;

        diagonal = sqrt(screenXSize**2 + screenYSize**2);


        car_img_number = 1;

        scale = img_scale_factors[car_img_number]*scaleMultiplier*diagonal*diagonalMultiplier;

        fname = os.path.join(get_package_share_directory('gps_visualization'),
         car_images[car_img_number])
        super(Car_visual,self).__init__("racecar",0,0,scale,fname,objectDraw);

        self.setZeroRotation(img_rotations[car_img_number]);
