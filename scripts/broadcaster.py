#!/usr/bin/env python
# insert MIT license here

import rospy
import psutil
from std_msgs.msg import String

def broadcaster():
    pub_psutil = rospy.Publisher('psutil', String, queue_size=10)
    rospy.init_node('broadcaster', anonymous=True)
    rate=rospy.Rate(10) # 10 hz
    while not rospy.is_shutdown():
        perf_str = "performance is performant %s" % rospy.get_time()
        rospy.loginfo(perf_str)
        pub_psutil.publish(perf_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        broadcaster()
    except rospy.ROSInterruptException:
        pass

