# Specification: The test checks whether the system is configured securely. The test passes
# if we cannot list the running ROS topics. If the test fails, the expected error
# is the AssertionError raised in this test, as well as a "Security Error" raised by ROS.
# If a different error than "Security Error" is raised by ROS, there is another error when
# attempting to list ROS topics.

import ros_topics
import subprocess

try:
    ros_topics.main()
    raise AssertionError("Should not be able to see any topics running if ROS security is enabled")
except subprocess.CalledProcessError:
    print("Test passed! We could did see any topics")
