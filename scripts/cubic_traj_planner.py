#!/usr/bin/env python

import rospy
import random

from ar_week5_test.msg import cubic_traj_params
from ar_week5_test.msg import cubic_traj_coeffs
from ar_week5_test.srv import compute_cubic_traj

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)
	compute_cubic(data)     #calling the function to execute the computation

def compute_cubic(data):

	compute = computation_client(data.p0,data.pf,data.v0,data.vf,data.t0,data.tf) #defining the compute variable
	pub=rospy.Publisher('coeffs',cubic_traj_coeffs,queue_size=10)     #initialising the publisher 
        print(compute)
        computed= cubic_traj_coeffs()  #defining the computed variables
	computed.a0=compute[0]
	computed.a1=compute[1]
	computed.a2=compute[2]
	computed.a3=compute[3]
	computed.t0=data.t0
	computed.tf=data.tf 

        rospy.loginfo(computed)  #display the messgae on the terminal
	pub.publish(computed)    #publish the message 

def computation_client(p0,pf,v0,vf,t0,tf):
    rospy.wait_for_service('compute_cubic')
    try:
        computation = rospy.ServiceProxy('compute_cubic', compute_cubic_traj)   #connecting to the service
        resp = computation(p0,pf,v0,vf,t0,tf)  #computing the trajectories using the data from subscriber
        return resp.a0, resp.a1, resp.a2, resp.a3
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)


def cubic_traj_planner():
	rospy.init_node('planner')    #initializing the publisher node
	rospy.Subscriber("params", cubic_traj_params,callback)   #subscribe to cubic_traj_params 
	rospy.spin()




if __name__ == '__main__':
	cubic_traj_planner()
