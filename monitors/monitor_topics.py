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

if __name__ == '__main__':
    output = subprocess.check_output(["ros2", "topic", "list"])
    print output

# if output:
#   raise AssertionError("Should not be able to see any nodes running. We saw the following nodes running:\n" + output)

# print 'OK. Did not see any nodes running'
