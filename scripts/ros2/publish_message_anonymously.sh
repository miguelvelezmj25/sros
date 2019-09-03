#!/bin/bash

# Run publisher ros2 node

ros2 topic pub -1 /secure_topic std_msgs/String "data: Should not see this message"
