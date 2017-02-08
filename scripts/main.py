#!/usr/bin/env python
#! -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import Int32

num = 0
count = 0
first = True

def cb(message, pub):
    global count
    global num
    global first
    first = False
    num += message.data
    if count %2 == 0: print "player1 : %d"%num
    elif count %2 == 1: print "player2 : %d"%num
    if num > 29:
        user = count%2 + 1
        print "player%d is Lose"%user
        pub.publish(1000)
    pub.publish(num)
    count += 1

if __name__ == '__main__':
    rospy.init_node('twice')
    pub = rospy.Publisher('pub', Int32, queue_size=1)
    sub = rospy.Subscriber('sub', Int32, cb, callback_args = pub)
    while first:
        pub.publish(num)
    rospy.spin()
