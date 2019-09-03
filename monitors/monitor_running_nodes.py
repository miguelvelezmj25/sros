#!/usr/bin/python

# Simple script to check the list of available ROS2 nodes. Raises an AssertionError if any nodes are listed.
#
# The script is currently used to check configuring the security of ROS2 using SROS. We observed that misconfiguring the
# environment can cause topics used for secured communication to be visible. This script checks if those topics are visible
# and raises an exception if they are.

import subprocess

if __name__ == '__main__':
  output = subprocess.check_output(["ros2", "node", "list"])

  if output:
    raise AssertionError("Should not be able to see any nodes running. We saw the following nodes running:\n" + output)

  print 'OK. Did not see any nodes running'
