#!/usr/bin/env python
# insert MIT license here

import rospy
import psutil
from msg_experiments.msg import cpu_times

def broadcaster():
    pub_psutil = rospy.Publisher('psutil', cpu_times, queue_size=10)
    rospy.init_node('broadcaster', anonymous=True)
    rate=rospy.Rate(10) # 10 hz
    while not rospy.is_shutdown():
        msg = cpu_times()
        state = psutil.cpu_times(True)
        msg.user = [s.user for s in state if hasattr(s, 'user')]
        msg.system = [s.system for s in state if hasattr(s, 'system')]
        msg.idle = [s.idle for s in state if hasattr(s, 'idle')]
        msg.nice = [s.nice for s in state if hasattr(s, 'nice')]
        msg.iowait = [s.iowait for s in state if hasattr(s, 'iowait')]
        msg.irq = [s.irq for s in state if hasattr(s, 'irq')]
        msg.softirq = [s.softirq for s in state if hasattr(s, 'softirq')]
        msg.steal = [s.steal for s in state if hasattr(s, 'steal')]
        msg.guest = [s.guest for s in state if hasattr(s, 'guest')]
        msg.guest_nice = [s.guest_nice for s in state if hasattr(s, 'guest_nice')]
        msg.interrupt = [s.interrupt for s in state if hasattr(s, 'interrupt')]
        msg.dpc = [s.dpc for s in state if hasattr(s, 'dpc')]
        
        rospy.loginfo(msg)
        pub_psutil.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        broadcaster()
    except rospy.ROSInterruptException:
        pass

