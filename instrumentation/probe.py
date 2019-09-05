# TODO not sure if needed
# import rclpy

callback_func = None


def instrumented_callback(msg):
    print('Will log that the callback to a subscriber was executed and the message received')
    global callback_func
    return callback_func(msg)


def instrument_callback(func):
    global callback_func
    callback_func = func
    return instrumented_callback


def create_node(rclpy, name):
    try:
        return rclpy.create_node(name)
    except RuntimeError as re:
        print('Will log that there was an error with creating the node')
        raise re

def publish(publisher, msg):
    print('Will log that the message sent is ' + msg.data)
    publisher.publish(msg)
