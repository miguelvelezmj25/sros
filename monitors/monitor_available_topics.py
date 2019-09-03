#!/usr/bin/python

# Simple script to check the list of running ROS2 nodes. Raises an AssertionError if any nodes are listed.
#
# The script is currently used to check configuring the security of ROS2 using SROS. We observed that despite configuring 
# the environement correctly, the name of "securely" running nodes can be retrieved from the running system and an attacker
# could initialize a node with one of the names listed in the results. Hence, this script should ALWAYS raise an exception
# even if the environment was configured to run with security enabled.
#
# Maybe, a better check would be to retrieve the list of running nodes and check if the ones that are running securely are
# not listed and the ones that are lists were not configured securely, either on purpose or by mistake.

import subprocess

TOPICS_TO_CHECK = ["/topic"]

if __name__ == '__main__':
    topics = subprocess.check_output(["ros2", "topic", "list"])
    topics_that_should_not_be_seen = []

    for topic in TOPICS_TO_CHECK:
        if topic in topics:
            topics_that_should_not_be_seen.append(topic)

    if topics_that_should_not_be_seen:
        raise AssertionError(
            "Should not be able to see that the topic " + str(topics_that_should_not_be_seen) + " is available")

    print 'OK. Did not see any topics that should not have not seen them.'
