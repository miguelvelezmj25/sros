# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import examples_rclpy_minimal_publisher.probe as probe
from time import sleep
import rclpy
from std_msgs.msg import String

# We do not recommend this style as ROS 2 provides timers for this purpose,
# and it is recommended that all nodes call a variation of spin.
# This example is only included for completeness because it is similar to examples in ROS 1.
# For periodic publication please see the other examples using timers.

def main(args=None):
    rclpy.init(args=args)
    #node = rclpy.create_node('authenticated_publisher')
    # WILL INSTRUMENT AUTOMATICALLY
    node = probe.Probe.create_node(rclpy, 'authenticated_publisher')
    publisher = node.create_publisher(String, 'secure_topic')

    msg = String()

    for i in range(0, 10):
        msg.data = 'Regular message ' + str(i)
        node.get_logger().info('Publishing: "%s"' % msg.data)
        # WILL INSTRUMENT AUTOMATICALLY
        #publisher.publish(msg)
        probe.Probe.publish(publisher, msg)
        sleep(0.5)  # seconds

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()