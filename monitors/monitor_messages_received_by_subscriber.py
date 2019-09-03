#!/usr/bin/python

# Simple script to check the messages that are received by a subscriber. Raises an AssertionError if an unexpected message
# is received.
#
# The script is currently used to check configuring the security of ROS2 using SROS. We observed that misconfiguring the
# environment can cause topics used for secured communication to be visible. This script checks if other nodes or sources,
# different from authenticated nodes, are sending messages that are not expected.
#
# This monitor does not test the case where an attacker is sending messages that "look like" messages that come from a
# trusted source, but are small enough to attach the system. For example, a pub sub system can be communicate how many
# resource should be allocated for a running process. An attacker could send messages that look valid to the subscriber,
# but requests the resources to be unnecessarily increased by a lot.

import subprocess

MESSAGE_THAT_SHOULD_NOT_BE_HEARD = "Should not see this message"

if __name__ == '__main__':
    messages = subprocess.check_output("ros2 run examples_rclpy_minimal_subscriber subscriber_old_school", shell=True)

    if MESSAGE_THAT_SHOULD_NOT_BE_HEARD in messages:
        raise AssertionError(
            "Should not be able to see the message \""
            + MESSAGE_THAT_SHOULD_NOT_BE_HEARD
            + "\" since it is not sent by the authenticated node")

    print 'OK. Did not see any messages that were not sent from the authenticated node.'
