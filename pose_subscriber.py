#!usr/bin/env python3
import rclpy 
from rclpy.node import Node
from turtlesim.msg import Pose
from std_msgs.msg import Float32

class PoseSubNode(Node):

    def __init__(self):
        super().__init__("pose_subscriber")

        self.pose_subscriber_ = self.create_subscription(
            Pose, "/turtle1/pose", self.pose_callback, 10)
        
        self.publisher = self.create_publisher(
            Float32, "/turtle1/distance_from_origin", 10)

    def pose_callback(self, msg):
        dis2 = (msg.x)**2 + (msg.y)**2
        self.get_logger().info("(" + str(msg.x) + ", " + str(msg.y) + ")")
        self.get_logger().info("Distance from origin: " + str(dis2**0.5))
        dis = dis2**0.5
        dis_msg = Float32()
        dis_msg.data = dis
        self.publisher.publish(dis_msg)




def main(args=None):
    rclpy.init(args=args)
    node = PoseSubNode()
    rclpy.spin(node)
    rclpy.shutdown()