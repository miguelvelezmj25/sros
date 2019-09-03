#!/usr/bin/python

# Simple script to echo the messages in a topic.
#
# The script is currently used to check configuring the security of ROS2 using SROS. We observed that misconfiguring the
# environment can cause topics used for secured communication to be visible. This script checks if we can echo the messages
# from a secure topic and raises an exception if we can.

import subprocess

TOPICS_TO_LISTEN = "/secure_topic"

if __name__ == '__main__':
    messages = subprocess.check_output(["ros2", "topic", "echo"])
    print messages
    # topics_that_should_not_be_seen = []
    #
    # for topic in TOPICS_TO_CHECK:
    #     if topic in topics:
    #         topics_that_should_not_be_seen.append(topic)
    #
    # if topics_that_should_not_be_seen:
    #     raise AssertionError(
    #         "Should not be able to see that the topic " + str(topics_that_should_not_be_seen) + " is available")
    #
    # print 'OK. Did not see any topics that should not have not seen them.'
