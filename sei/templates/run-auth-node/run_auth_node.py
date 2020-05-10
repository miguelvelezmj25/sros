import rclpy
import <node_module>
from time import sleep

rclpy.init(args=None)

try:
    node = <node_module>.<run_function>
    sleep(2)
    node.destroy_node()
except RuntimeError:
    rclpy.shutdown()
    raise AssertionError("If a RuntimeError is raised, the node is not authenticated nor authorized to execute")

print('If no error is raise, the system is not configured securely')
rclpy.shutdown()