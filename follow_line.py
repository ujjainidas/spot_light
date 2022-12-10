import rospy
import socket
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import PointCloud2
# from simple_pid import PID		

class itl_run:

    def __init__(self) -> None:
        self.error = 0

        self.port = 6000	

        self.s = socket.socket()
        self.s.connect(('127.0.0.1', self.port))	

        self.msg = Twist()
        self.msg.angular.x = 0.0 # yaw
        self.msg.angular.y = 0.0
        self.msg.angular.z = 0.0
        self.msg.linear.x = 0.0
        self.msg.linear.y = 0.0
        self.msg.linear.z = 0.0 # forward and back
        # self.pid = PID(1, 0.1, 0.05, setpoint=1)

    # def callback(self, data):
    #     self.error = data.data
    #     print(self.error)
    #     rospy.loginfo("The error is %f", float(self.error))

    def run_prog(self):
        ros_pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        rospy.init_node('node_camera_sub', anonymous=True)
        # ros_key = rospy.Subscriber('node_camera', String, self.callback)
        rate = rospy.Rate(60)
        while not rospy.is_shutdown():
            print(self.error)
            self.msg.linear.x = 0.3

            error_str = self.s.recv(1024).decode()

            # end_index = 0
            # for i in range(0, len(error_str)): 
            #     if error_str[i] == 0:
            #         end_index = i
            #         break
            
            # if end_index > 1:
            self.error = error_str[0:4]
            self.msg.angular.z = -float(self.error)
            print(self.msg.angular.z)

            print("running robot")

            ros_pub.publish(self.msg)
            rate.sleep()
        self.s.close()

if __name__ == '__main__':
    app_prog = itl_run()
    app_prog.run_prog()
        # rospy.init_node('spot_cmd_vel')
