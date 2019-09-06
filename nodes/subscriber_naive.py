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

import functools
import examples_rclpy_minimal_subscriber.probe_attacker as probe
import rclpy

from std_msgs.msg import String

g_node = None


def chatter_callback(msg):
    global g_node
    g_node.get_logger().info('This is the message: "%s"' % msg.data)

def main(args=None):
    global g_node
    rclpy.init(args=args)

    # WILL INSTRUMENT AUTOMATICALLY
    #g_node = rclpy.create_node('naive_subscriber')
    g_node = probe.Probe.create_node(rclpy, 'naive_subscriber')

    # WILL INSTRUMENT AUTOMATICALLY
    #subscription = g_node.create_subscription(String, 'secure_topic', chatter_callback)
    subscription = g_node.create_subscription(String, 'secure_topic', probe.Probe.instrument_callback(chatter_callback))
    subscription  # prevent unused variable warning

    i = 0
    while i < 5:
        rclpy.spin_once(g_node)
        i+= 1

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    # WILL INSTRUMENT AUTOMATICALLY
    #g_node.destroy_node()
    probe.Probe.destroy_node(g_node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()