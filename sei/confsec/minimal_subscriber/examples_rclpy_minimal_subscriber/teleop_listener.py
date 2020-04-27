import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class TeleopListener(Node):

    def __init__(self):
        super().__init__('teleop_listener')
        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, twist):
        self.get_logger().info('Linear velocity: %.2f\t Angular velocity: %.2f' % (twist.linear.x, twist.angular.z))


def main(args=None):
    rclpy.init(args=args)

    teleop_listener = TeleopListener()

    rclpy.spin(teleop_listener)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    teleop_listener.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()