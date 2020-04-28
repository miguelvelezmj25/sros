# Specification: The test checks whether the system is configured securely. The test passes
# if the teleop_listener node is created successfully. If the test fails, the expected error
# must indicate a "SECURITY ERROR" when creating a node. If some other error message appears,
# then there might be another error besides a security related error.

import rclpy
import teleop_listener
from time import sleep

rclpy.init(args=None)

try:
    node = teleop_listener.TeleopListener()
    sleep(2)
    node.destroy_node()
except RuntimeError:
    rclpy.shutdown()
    raise AssertionError("Could not create a teleop_listener node")

print('Test passed! Created a teleop_listener node')
rclpy.shutdown()