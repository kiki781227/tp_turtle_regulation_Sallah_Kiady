#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import math
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool
    
class MyPublisherNode(Node):
    def __init__(self):
        super().__init__("first_pub")
        self.publisher_=self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.publisher_moving = self.create_publisher(Bool, "/turtle1/is_moving", 10)
        self.subscriber_=self.create_subscription(Pose, "/turtle1/pose", self.sub_callback, 10)
        self.create_timer(0.5, self.publisher_callback)
        self.x_wp = 7
        self.y_wp = 7
        self.kp = 2
        self.kpl = -1
        self.turtle_pose=Pose()
        self.get_logger().info("publisher has started")
       


    def sub_callback(self, msg):
        self.turtle_pose=msg

    def publisher_callback(self):
        rep = Twist()
        theta_desired = self.angle_desired()
        theta_turtle = self.turtle_pose.theta
        distance_tolerance = 0.5
        distance = self.distance()

        is_moving_msg = Bool()

        if distance > distance_tolerance:

            rep.linear.x = self.kpl * distance
            rep.angular.z = self.commande_cap(theta_desired, theta_turtle) * self.kp
            self.publisher_.publish(rep)
            is_moving_msg.data = True
            self.publisher_moving.publish(is_moving_msg)
        else:
            is_moving_msg.data = False  # La tortue est arrêtée
            self.publisher_moving.publish(is_moving_msg)

    def angle_desired(self):
        
        angle = math.atan2(self.turtle_pose.y - self.y_wp , self.turtle_pose.x - self.x_wp)
        return angle
    
    def commande_cap(self, t_cible, t_actuel):
        e = math.atan(math.tan((t_cible - t_actuel) / 2))
        return e

    def distance(self):
        e1 = math.sqrt((self.turtle_pose.x - self.x_wp) ** 2 + (self.turtle_pose.y - self.y_wp) ** 2)
        v = e1
        return v

        


def main(args=None):
    rclpy.init(args=args)
    node = MyPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()