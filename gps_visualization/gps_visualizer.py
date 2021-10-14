

# ROS Client Library for Python
from math import pi
from game_engine.Object2D import Object2D
from iac_visualization_frame import IAC_visualization_frame


 
 import rclpy

# Handles the creation of nodes
from rclpy.node import Node
  
# Handles string messages


 
from std_msgs.msg import String
from novatel_oem7_msgs.msg import BESTPOS as posdata
from novatel_oem7_msgs.msg import HEADING as headingMsgType

from math import atan2

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
 
    #self.declare_parameter("usingIMSMap",True);
    #self.declare_parameter("first_person",False);


    useIMS = False;


    # create simulation
    self.frame1 = IAC_visualization_frame(useIMS=useIMS,first_person=True);


    # create sub to gps data
    

    self.odom_subscriber = self.create_subscription(posdata, '/novatel_top/bestpos', self.gps_callback, 20)
    self.odom_subscriber  # prevent unused variable warning

    self.heading_subscriber = self.create_subscription(headingMsgType, '/novatel_top/heading', self.heading_callback, 20)
    self.heading_subscriber
    
  
  def gps_callback(self, msg):

    # get data from ros message
    lattitude = msg.lat;
    longitude = msg.lon;
    #altitude = msg.hgt;
    
    # set the position of the car by using the track object to convert
    self.frame1.updateCarPos(lattitude,longitude);
    

  
  def heading_callback(self, msg):
    
    # TODO get heading from msg here
    heading = 0;

    # TODO convert heading to degrees

    self.frame1.updateCarHeading(heading);



    








 
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



