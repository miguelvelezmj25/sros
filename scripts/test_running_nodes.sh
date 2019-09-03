#!/bin/bash

# Execute scripts to test the nodes that are running

./run_publisher.sh &
sleep 2
./monitor_running_nodes.sh &
