#!/usr/bin/env bash

ros2 run examples_rclpy_minimal_subscriber laser_listener

cd ~/crypto
python crypt.py -e
sshpass -p 'mvelezce' scp laser_logs.txt mvelezce@172.16.94.130:~/crypto