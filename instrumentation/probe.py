# Template for probes

class Probe:
    CALLBACK_FUNC = None

    @staticmethod
    def destroy_node(node):
        print('Will log that node was destroyed')
        node.destroy_node()

    @staticmethod
    def instrumented_callback(msg):
        print('Will log that the callback to a subscriber was executed and the message received')
        return Probe.CALLBACK_FUNC(msg)

    @staticmethod
    def instrument_callback(func):
        Probe.CALLBACK_FUNC = func
        return Probe.instrumented_callback

    @staticmethod
    def create_node(rclpy, name):
        try:
            return rclpy.create_node(name)
        except RuntimeError as re:
            print('Will log that there was an error with creating the node')
            raise re

    @staticmethod
    def publish(publisher, msg):
        print('Will log that the message sent is ' + msg.data)
        publisher.publish(msg)
