import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import PointCloud2
# from simple_pid import PID

class itl_run:

    def __init__(self) -> None:
        self.error = 0
        self.msg = Twist()
        self.msg.angular.x = 0.0 # yaw
        self.msg.angular.y = 0.0
        self.msg.angular.z = 0.0
        self.msg.linear.x = 0.0
        self.msg.linear.y = 0.0
        self.msg.linear.z = 0.0 # forward and back
        # self.pid = PID(1, 0.1, 0.05, setpoint=1)

    def callback(self, data):
        self.error = data.data
        print(self.error)
        rospy.loginfo("The error is %f", float(self.error))

    def run_prog(self):
        ros_pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        rospy.init_node('node_camera_sub', anonymous=True)
        ros_key = rospy.Subscriber('node_camera', String, self.callback)
        rate = rospy.Rate(60)
        while not rospy.is_shutdown():
            print(self.error)
            self.msg.linear.x = 0.3

            self.msg.angular.z = float(self.error)

            print("running robot")

            ros_pub.publish(self.msg)
            rate.sleep()
if __name__ == '__main__':
    app_prog = itl_run()
    app_prog.run_prog()
        # rospy.init_node('spot_cmd_vel')
