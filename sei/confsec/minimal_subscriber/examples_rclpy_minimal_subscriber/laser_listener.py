import time
import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan
from rclpy.qos import QoSProfile
from rclpy.qos import QoSReliabilityPolicy

laser_file = open("/home/mvelezce/crypto/laser_logs.txt", "w")

class LaserListener(Node):

    def __init__(self):
        super().__init__('laser_listener')
        self.subscription = self.create_subscription(
            LaserScan,
            'scan',
            self.listener_callback,
            QoSProfile(depth=10, reliability=QoSReliabilityPolicy.BEST_EFFORT))
        self.subscription  # prevent unused variable warning

    def listener_callback(self, scan):
        self.get_logger().info('Laser time %s' % scan.header.stamp.sec)
        laser_file.write(str(scan.header.stamp.sec))
        laser_file.write('\n')


def main(args=None):
    rclpy.init(args=args)

    laser_listener = LaserListener()

    for i in range(0, 5):
        rclpy.spin_once(laser_listener)
        time.sleep(1)

    laser_file.close()


    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    laser_listener.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()