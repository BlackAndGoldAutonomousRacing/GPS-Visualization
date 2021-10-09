from game_engine.Sprite import Sprite
import pymap3d as p3d


'''
Finding coords for tracks:
https://earth.google.com/web/search/Indianapolis+Motor+Speedway,+West+16th+Street,+Indianapolis,+IN/@39.79749239,-86.23331699,219.1043837a,1169.72532299d,35y,0h,0t,0r/data=CigiJgokCVa07OC2uz1AEZG8YtDoWyHAGRtBYOW4H0XAIUV1CJoNeGPA
https://gps-coordinates.org/coordinate-converter.php
'''

class Racetrack(Sprite):
    def __init__(self,objectDraw,useIMS=True):

        
        screenXSize = objectDraw.screenSizeX;
        screenYSize = objectDraw.screenSizeY;

       
        picSrc = "";
        if (useIMS):
            picSrc = "assets/IMS.png";

            # lat and long at the upper left and bottom right corners of the image
            self.trackRefLat = 39.802499999999995; # 39 48 09 N
            self.trackRefLong = -86.24138888888889;# 86 14 29 W
            trackRefLatEnd = 39.7875; # 39 48 09 N
            trackRefLongEnd = -86.22694444444444;# 86 14 29 W

            # pixel dimensions of the image
            self.picDimX = 539.0; #pixels
            self.picDimY = 742.0; # pixels

            # scales the image by this factor
            self.scale = float(screenXSize)/self.picDimX;

            # find the dimensions of the track in ned units
            self.real_trackYWidth, self.real_trackXWidth,z = p3d.geodetic2ned(trackRefLatEnd, trackRefLongEnd,0,self.trackRefLat,self.trackRefLong,0);
            self.real_trackXWidth = abs(self.real_trackXWidth);
            self.real_trackYWidth = abs(self.real_trackYWidth);

            #print("real trackwidth: ", self.real_trackXWidth, self.real_trackYWidth);

        else:
            # TODO finish LOR case
            print("LOR case in racetrack.py not finished");


        #print("scale:",self.scale)
        super(Racetrack,self).__init__("racetrack",objectDraw.screenSizeX/2,objectDraw.screenSizeY/2,self.scale,picSrc);

        objectDraw.add(self);


    def getTrackRelativePosition(self,lat, long, alt=0):

        #print("lat,long,alt: ", lat,long,alt);

        y_real,x_real,z = p3d.geodetic2ned(lat,long,alt,self.trackRefLat, self.trackRefLong,0); # lat,long,alt -> north,east,down wrt trackRef
        y_real = -y_real; # y is negative because in the engine south is a positive y

        #print("x,y real: ",x_real,y_real);

        conversion_x = self.picDimX*self.scale/self.real_trackXWidth;
        conversion_y = self.picDimY*self.scale/self.real_trackYWidth;

        #print("conv x,y : ",conversion_x, conversion_y);
        x = (x_real)*conversion_x;
        y = (y_real)*conversion_y;
        
        #print("x,y: ", x, y);


        track_position = self.getPosition();

        #print("track size ", self.xSize, self.ySize);

        #print("racetrack pos: ", track_position);
        x_rel = x - self.xSize/2.0 + track_position[0];
        y_rel = y - self.ySize/2.0 + track_position[1];
        
        #print("x_rel, y_rel: ", x_rel, y_rel);
  
        return x_rel,y_rel;