#!/usr/bin/env python
#! -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import Int32

def flag(message, pub):
    print "Prease enter the number 1～3"
    i = int(raw_input())
    if i > 0 and i < 4:
        pub.publish(i)
    else:
        print "enter 1～3"

if __name__ == '__main__':
    rospy.init_node('player1')
    pub = rospy.Publisher('sub', Int32, queue_size=1)
    sub = rospy.Subscriber('pub', Int32, flag, callback_args = pub)
    rospy.spin()
