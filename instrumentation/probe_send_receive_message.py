# Probe variant to use in tests to send and receive messages from an authenticated node

class Probe:
    CALLBACK_FUNC = None
    AUTHENTICATED_MESSAGE = 'should be sent and received'
    RECEIVED_MESSAGE = False

    @staticmethod
    def destroy_node(node):
        node.destroy_node()

        if not Probe.RECEIVED_MESSAGE:
            print('Will log that the authenticated message was NOT received')
            raise AssertionError('Did not receive the authenticated message')

    @staticmethod
    def instrumented_callback(msg):
        if Probe.AUTHENTICATED_MESSAGE != msg.data:
            return Probe.CALLBACK_FUNC(msg)

        Probe.RECEIVED_MESSAGE = True
        print('Will log that the authenticated message that was sent was received')

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
        publisher.publish(msg)

        print('Sending message ' + Probe.AUTHENTICATED_MESSAGE)
        msg.data = Probe.AUTHENTICATED_MESSAGE
        publisher.publish(msg)
