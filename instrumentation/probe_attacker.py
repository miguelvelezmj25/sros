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
    def instrument_callback(func):
        Probe.CALLBACK_FUNC = func
        return Probe.instrumented_callback

    @staticmethod
    def create_node(rclpy, name):
        try:
            node = rclpy.create_node(name)
            print('Will log an AssertionError: the node should not be create since it is not authenticated')
            return node
        except RuntimeError as re:
            print('Will log that there was an error with creating the node')
            raise re

    @staticmethod
    def publish(publisher, msg):
        publisher.publish(msg)

        print('Will log that we sent attacker message ' + Probe.ATTACKER_MESSAGE)
        msg.data = Probe.ATTACKER_MESSAGE
        publisher.publish(msg)
        