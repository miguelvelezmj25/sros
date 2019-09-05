# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import examples_rclpy_minimal_publisher.probe as probe
import rclpy

from std_msgs.msg import String

g_node = None

def chatter_callback(msg):
    global g_node
    g_node.get_logger().info('This is the message: "%s"' % msg.data)

def main(args=None):
    global g_node
    rclpy.init(args=args)

    #g_node = rclpy.create_node('authenticated_subscriber')
    # WILL INSTRUMENT AUTOMATICALLY
    g_node = probe.create_node(rclpy, 'authenticated_subscriber')

    #subscription = g_node.create_subscription(String, 'secure_topic', chatter_callback)
    # WILL INSTRUMENT AUTOMATICALLY
    subscription = g_node.create_subscription(String, 'secure_topic', probe.instrument_callback(chatter_callback))
    subscription  # prevent unused variable warning

    rclpy.spin_once(g_node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    g_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()