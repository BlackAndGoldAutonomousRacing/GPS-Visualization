

# ROS Client Library for Python
from math import pi
from .game_engine.Object2D import Object2D
from .iac_visualization_frame import IAC_visualization_frame



import rclpy

# Handles the creation of nodes
from rclpy.node import Node

# Handles string messages



from std_msgs.msg import String
from deep_orange_msgs.msg import Telemetry

from math import atan2

from .car_visual import Car_visual
from .game_engine.ObjectDraw import ObjectDraw
from .game_engine.Sprite import Sprite
from .racetrack import Racetrack






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


    self.data_subscriber = self.create_subscription(Telemetry, '/telemetry/vehicle_state', self.telemetry_callback, 20)
    self.data_subscriber  # prevent unused variable warning


  def telemetry_callback(self, msg):

    # get data from ros message
    latitude = msg.latitude;
    longitude = msg.longitude;
    #altitude = msg.hgt;

    # set the position of the car by using the track object to convert
    self.frame1.updateCarPos(latitude,longitude);
    self.frame1.updateCarHeading(msg.current_yaw);


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
