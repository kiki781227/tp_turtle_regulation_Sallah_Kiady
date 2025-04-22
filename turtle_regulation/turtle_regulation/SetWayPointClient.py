import rclpy
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute

class TurtleClient(Node):
    def __init__(self):
        super().__init__('turtle_client')
        self.client = self.create_client(TeleportAbsolute, '/turtle1/teleport_absolute')

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service...')

        self.send_request()

    def send_request(self):
        request = TeleportAbsolute.Request()
        request.x = 5.0  # Nouvelle position X
        request.y = 5.0  # Nouvelle position Y
        request.theta = 1.57  # Nouvelle orientation (90°)

        future = self.client.call_async(request)
        future.add_done_callback(self.callback)

    def callback(self, future):
        self.get_logger().info('Turtle teleported successfully!')
        rclpy.shutdown()  # Arrêter le node après exécution

def main(args=None):
    rclpy.init(args=args)
    node = TurtleClient()

if __name__ == '__main__':
    main()