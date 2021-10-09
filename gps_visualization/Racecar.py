
'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     Final Project
	Author:         Alec Pannunzio, afpannun@purdue.edu
	Team ID:        LC4-5 
===============================================================================
'''
from math import sqrt,cos,sin,pi
from game_engine.RelativeSprite import RelativeSprite
import pygame

# it's a racecar! (Vroom vroom) -  basically just sets up the RelativeSprites to be used as a racecar
# note: must call setRaceTrack() for track awareness to work
'''
class members:
raceCarImg - pygame.Surface - the image of a racecar to be used for the sprite
racetrack - Racetrack - the racetrack we will be driving on  ;   for figuring out if we are on the track and CPU driving
racetrackSet - boolean - whether we have set a racetrack yet
'''


class Racecar(RelativeSprite):
    def __init__(self,objectDraw,isFirstPerson,scale,racecar_source):
        screenXSize = objectDraw.screenSizeX;
        screenYSize = objectDraw.screenSizeY;
            
        super(Racecar,self).__init__("racecar", screenXSize/2,screenYSize/2,scale,racecar_source,objectDraw);

                
        self.racetrack = None;
        self.racetrackSet = False;

    # sets the racetrack and allows track awareness to work
    def setRacetrack(self, racetrack):
        self.racetrack = racetrack;
        self.racetrackSet = True;




'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
