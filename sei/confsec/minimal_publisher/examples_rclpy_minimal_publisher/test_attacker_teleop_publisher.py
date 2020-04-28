# Specification: The test checks whether the system is configured securely. The test passes
# if the attacker_teleop_publisher node is NOT created successfully. If the test fails, the
# expected error is the AssertionError raised in this test.

import attacker_teleop_publisher

try:
    attacker_teleop_publisher.main()
    raise AssertionError("Should not be able to create an attacker_teleop_publisher node")
except RuntimeError:
    print('Test passed! Could not create an attacker_teleop_publisher node')