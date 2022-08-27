#!/usr/bin/env python

import rospy
import random
import numpy as np
from ar_week5_test.msg import cubic_traj_params
#function to publish the message
def points_generator(): 
#defining a topic to which message will be published  
    pub = rospy.Publisher('params', cubic_traj_params, queue_size=10)
#initializing the publisher node and setting anonymous = True will append random integers at the end ofour publisher node
    rospy.init_node('generator')
    rate= rospy.Rate(0.05)  #publishes at the rate of 20 message per second
    cubic= cubic_traj_params()
    while not rospy.is_shutdown():
	cubic.p0= np.random.uniform(-10 ,10)
	cubic.pf= np.random.uniform(-10 ,10)
	cubic.v0= np.random.uniform(-10 ,10)
	cubic.vf= np.random.uniform(-10 ,10)
	cubic.t0= 0
	cubic.tf= cubic.t0 + round(np.random.uniform(5 ,10))
	rospy.loginfo(cubic)     #display the messgae on the terminal
	pub.publish(cubic)       #publish the message 
	rate.sleep()             #will wait enough enough untill the node publishes the message

if __name__ == '__main__':
    try:
        points_generator()
    except rospy.ROSInterruptException:  #capture the interruption signal
        pass
