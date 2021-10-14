




from math import pi

from numpy.lib.histograms import _unsigned_subtract
from game_engine.Object2D import Object2D
from iac_visualization_frame import IAC_visualization_frame





from car_visual import Car_visual
from game_engine.ObjectDraw import ObjectDraw
from game_engine.Sprite import Sprite
from racetrack import Racetrack

from math import atan2

testing = True;



class Gps_visualizer():
  """
  Create a subscriber node
  """
    

  def __init__(self):
 
 
 
    #self.declare_parameter("usingIMSMap",True);
    #self.declare_parameter("first_person",False);

    useIMS = False;

    # create simulation
    self.frame1 = IAC_visualization_frame(useIMS=useIMS,first_person=False);


    # create sub to gps data
    
    if (not testing):
      self.odom_subscriber = self.create_subscription(posdata, '/novatel_top/bestpos', self.gps_callback, 20)
      self.odom_subscriber  # prevent unused variable warning

      self.heading_subscriber = self.create_subscription(headingdata, '/novatel_top/heading', self.heading_callback, 20)
      self.heading_subscriber
    else:
      
      i = 0;
      while(not self.frame1.objectDraw.done or self.frame2.objectDraw.done):
        self.frame1.run();

        i+= 1;
       
        if (useIMS):
            if (i == 10): # move the car to the pits
                self.frame1.updateCarPos(39.79055555555556,-86.23861111111111);

            elif (i == 20): # move the car to the center of the dirt track
                self.frame1.updateCarPos(39.799166666666665,-86.23222222222222);
            elif (i==30):
                self.frame1.updateCarPos(39.793148,-86.238868);
        else:
            if (i == 1): # move the car to the pits
                self.frame1.updateCarPos(39.812523,-86.341831);

       

        self.frame1.updateCarHeading(180 + 180 * atan2(self.frame1.car_visual.yPosition - self.frame1.racetrack.yPosition,self.frame1.car_visual.xPosition - self.frame1.racetrack.xPosition)/pi)
       
  
  def gps_callback(self, msg):

    # get data from ros message
    lattitude = msg.lat;
    longitude = msg.lon;
    #altitude = msg.hgt;
    
    # set the position of the car by using the track object to convert
    self.frame1.updateCarPos(lattitude,longitude);
    

  
  def heading_callback(self, msg):
    
    # TODO get heading from msg here
    heading = msg.data;

    # TODO convert heading to degrees

    self.frame1.updateCarHeading(heading);



    








 
def main(args=None):
 
 
 
  # Create a subscriber
 

    gps_visualizer = Gps_visualizer()

    gps_visualizer.__init__();

 
if __name__ == '__main__':
  main()


