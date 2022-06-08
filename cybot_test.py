#!/usr/bin/env python
# license removed for brevity
import rospy
import time
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('/cybot_btt_cmd', String, queue_size=10)
    rospy.init_node('serial_node', anonymous=True)
    rate = rospy.Rate(10) # 10hz 
    hello_str = "MOVE<X>2000</X>" 
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    rate.sleep()
    time.sleep(2)
    hello_str = "MOVE<X>-2000</X>" 
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    rate.sleep()
    time.sleep(2)
    hello_str = "MOVE<Y>2000</Y>" 
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    rate.sleep()
    time.sleep(2)
    hello_str = "MOVE<Y>-2000</Y>" 
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    rate.sleep()
    time.sleep(2)
    hello_str = "MOVE<Z>2000</Z>" 
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    rate.sleep()
    time.sleep(2)
    hello_str = "MOVE<Z>-2000</Z>" 
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    rate.sleep()
    time.sleep(2)
    hello_str = "MOVE<E0>2000</E0>" 
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    rate.sleep()
    time.sleep(2)
    hello_str = "MOVE<E0>-2000</E0>" 
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    rate.sleep()
    time.sleep(2)
    hello_str = "MOVE<E1>2000</E1>" 
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    rate.sleep()
    time.sleep(2)
    hello_str = "MOVE<E1>-2000</E1>" 
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    rate.sleep()
    time.sleep(2)
    hello_str = "MOVE<E2>2000</E2>" 
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    rate.sleep()
    time.sleep(2)
    hello_str = "MOVE<E2>-2000</E2>" 
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    rate.sleep()
    time.sleep(2)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
