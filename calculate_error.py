import rospy
from std_msgs.msg import String
import tty, sys, termios

if __name__ == '__main__':
    ros_pub = rospy.Publisher('node_camera', String, queue_size=10)
    rospy.init_node('node_camera_pub')
    rate = rospy.Rate(60)
    x = 0
    while not rospy.is_shutdown():
        ros_pub.publish(x)
        rate.sleep()
