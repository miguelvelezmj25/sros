#!/bin/bash

# Execute scripts to test publishing a message

echo "Running the script to monitor the messages received by a subscriber"
../monitor/monitor_messages_received_by_subscriber.sh &
echo "Waiting 2 seconds for the above monitor to start a node to begin listening to messages"
sleep 2
echo "Running the script to publish a message anonymously"
../ros2/publish_message_anonymously.sh
# TODO send message from authenticated node. This is still bad since I found out the name of the node and was able to send a message without any issue
echo "Done testing"

#echo "Send message from the environement"
#echo "There will be an error if misconfigured"
#echo "Send message from authenticated node"
#echo "No error"
