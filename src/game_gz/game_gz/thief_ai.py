#!/usr/bin/env python3

import random
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from ros_gz_interfaces.msg import Contacts


class RandomThief(Node):

    def __init__(self):
        super().__init__("random_thief")

        self.caught = False

        self.cmd_pub = self.create_publisher(
            Twist,
            "/thief/cmd_vel",
            10
        )
        self.contact_sub = self.create_subscription(
            Contacts,
            "/world/duniya_ek/model/chitti/link/base_link/sensor/contact_sensor/contact",
            self.contact_callback,
            10
        )

        self.timer = self.create_timer(1.0, self.gameloop)

    def gameloop(self):
        msg = Twist()

        if self.caught:
            cmd = Twist()
            cmd.linear.x = 0.0
            cmd.angular.z = 0.0
            self.cmd_pub.publish(cmd)
            self.get_logger().info("GAME OVER")
            return

        msg.linear.x = random.uniform(-0.5, 1.0)
        msg.angular.z = random.uniform(-1.5, 1.5)

        self.cmd_pub.publish(msg)
    
    def contact_callback(self, msg):
        if len(msg.contacts) > 0:
            self.caught = True


def main(args=None):
    rclpy.init(args=args)
    node = RandomThief()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()