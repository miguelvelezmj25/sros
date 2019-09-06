# Probe variant to use in tests when sending a message from an attacker node and checking if the message was received by another node

class Probe:
    CALLBACK_FUNC = None
    ATTACKER_MESSAGE = 'malicious data'
    RECEIVED_MESSAGE = False

    @staticmethod
    def destroy_node(node):
        node.destroy_node()

        if Probe.RECEIVED_MESSAGE:
            print('Will log that the attacker message WAS received')
            raise AssertionError('Receive the attacker message')

    @staticmethod
    def instrumented_callback(msg):
        if Probe.ATTACKER_MESSAGE != msg.data:
            return Probe.CALLBACK_FUNC(msg)

        Probe.RECEIVED_MESSAGE = True
        print('Will log that the attacker message that was sent was received')

    @staticmethod
    def create_node(rclpy, name):
        try:
            node = rclpy.create_node(name)
            print('Will log an AssertionError: the node should not be create since it is not authenticated')
            return node
        except RuntimeError as re:
            print('Will log that this behavior is intended since the node should not have been created')
            raise re

    @staticmethod
    def publish(publisher, msg):
        publisher.publish(msg)

        print('Will log that we sent attacker message ' + Probe.ATTACKER_MESSAGE)
        msg.data = Probe.ATTACKER_MESSAGE
        publisher.publish(msg)
