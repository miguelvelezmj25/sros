from time import sleep

import rclpy

from geometry_msgs.msg import Twist

def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('attacker_teleop_publisher')
    publisher = node.create_publisher(Twist, 'cmd_vel', 10)

    sleep(2)
    twist = Twist()
    twist.linear.x = 0.2
    twist.linear.y = 0.0
    twist.linear.z = 0.0

    publisher.publish(twist)
    sleep(1)  # seconds

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()