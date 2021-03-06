#!/bin/bash

# Execute scripts to test the nodes that are running

echo "Running the ROS2 node that publishes messages"
../ros2/run_publisher.sh &
echo "Waiting 2 seconds for the above node to start publishing messages"
sleep 2
echo "Running the script to check the running nodes"
../monitor/monitor_running_nodes.sh &
sleep 10
echo "Done testing"