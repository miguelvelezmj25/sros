# Specification: The test checks whether the system is configured securely. The test passes
# if we cannot list the running ROS nodes. If the test fails, the expected error
# is the AssertionError raised in this test, as well as a "Security Error" raised by ROS.
# If a different error than "Security Error" is raised by ROS, there is another error when
# attempting to list ROS nodes.

import ros_nodes
import subprocess

try:
    ros_nodes.main()
    raise AssertionError("Should not be able to see any nodes running if ROS security is enabled")
except subprocess.CalledProcessError:
    print("Test passed! We did not see any nodes")
