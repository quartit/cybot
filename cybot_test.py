#!/usr/bin/env python
# license removed for brevity
import rospy
import time
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('/cybot_btt_cmd', String, queue_size=10)
    rospy.init_node('serial_node', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    #while not rospy.is_shutdown():
    hello_str = "MOVE<E2>-4000</E2><E0>15000</E0><E1>-15000</E1>" 
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    rate.sleep()
    time.sleep(2)
    hello_str = "MOVE<E2>4000</E2><E0>-15000</E0><E1>15000</E1>" 
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
