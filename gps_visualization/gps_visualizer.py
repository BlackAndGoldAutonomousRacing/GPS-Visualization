

'''
This allows the code to compile without the rosbag play dependencies
'''
testing = True;









# ROS Client Library for Python
import rclpy
 
# Handles the creation of nodes
from rclpy.node import Node
 
# Handles string messages
from std_msgs.msg import String

if (not testing):
  from novatel_oem7_msgs.msg import BESTPOS as posdata


from car_visual import Car_visual
from game_engine.ObjectDraw import ObjectDraw
from game_engine.Sprite import Sprite
from racetrack import Racetrack



class Gps_visualizer(Node):
  """
  Create a subscriber node
  """
    

  def __init__(self):
 
    # Initiate the Node class's constructor and give it a name
    super().__init__('gps_visualizer')
 
  
    # create sub to gps data
    
    if (not testing):
      self.odom_subscriber = self.create_subscription(posdata, '/novatel_top/duplicate/bestpos', self.gps_visualizer_callback, 20)
      self.odom_subscriber  # prevent unused variable warning


    # Init simulation

    screenXSize = 500;
    screenYSize = 1000;
    self.objectDraw = ObjectDraw(screenXSize, screenYSize);
    self.racetrack = Racetrack(self.objectDraw, True); # True for IMS, False for LOR
    self.car_visual = Car_visual(self.objectDraw);
    self.objectDraw.setBackgroundColor((0,255,0));



    # start the simulation
    self.objectDraw.start();


    if (testing):
      i = 0;
      while(not self.objectDraw.done):
        self.objectDraw.run();
        i+= 1;

        if (i == 60): # move the car to the pits
          self.car_visual.setPosition(self.racetrack.getTrackRelativePosition(39.79055555555556,-86.23861111111111));
        elif (i == 120): # move the car to the center of the dirt track
          self.car_visual.setPosition(self.racetrack.getTrackRelativePosition(39.799166666666665,-86.23222222222222));
          pass;

      


  
  def gps_visualizer_callback(self, msg):

    # get data from ros message
    lattitude = msg.lat;
    longitude = msg.lon;
    #altitude = msg.hgt;
    
    # set the position of the car by using the track object to convert
    self.car_visual.setPosition(self.racetrack.getTrackRelativePosition(lattitude,longitude));

    # update the viewpane
    self.objectDraw.run();
    


    








 
def main(args=None):
 
  # Initialize the rclpy library
  rclpy.init(args=args)
 
  # Create a subscriber
  gps_visualizer = Gps_visualizer()
 
  # Spin the node so the callback function is called.
  # Pull messages from any topics this node is subscribed to.
  rclpy.spin(gps_visualizer)
 
  # Destroy the node explicitly
  # (optional - otherwise it will be done automatically
  # when the garbage collector destroys the node object)
  gps_visualizer.destroy_node()
   
  # Shutdown the ROS client library for Python
  rclpy.shutdown()
 
if __name__ == '__main__':
  main()



