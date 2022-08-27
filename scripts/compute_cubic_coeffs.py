#!/usr/bin/env python

import rospy
from ar_week5_test.msg import cubic_traj_coeffs
from ar_week5_test.srv import compute_cubic_traj, compute_cubic_trajResponse
import numpy as np

def handle_computation(req):
    #creating the two matrices
    a = np.matrix([[req.p0], [req.v0], [req.pf], [req.vf]]) 
    b = np.matrix([[1, req.t0, req.t0**2, req.t0**3],
		   [0,1,2*req.t0, 3*req.t0**2],
		   [1,req.tf,req.tf**2, req.tf**3],
	  	   [0,1,2*req.tf,3*req.tf**2]])
    #multipying two matrices
    c = np.array(np.dot(np.linalg.inv(b),a)) 
    print('Best coefficents computated : a0 = {} a1 = {} a2 = {} a3 = {}'.format(c[0][0],c[1][0],c[2][0],c[3][0]))
    return compute_cubic_trajResponse(a0=c[0][0],a1=c[1][0],a2=c[2][0],a3=c[3][0])



def compute_cubic_coeffs():
	rospy.init_node("computer")   #initialising the node 
	service= rospy.Service("compute_cubic" , compute_cubic_traj , handle_computation) #initialising the service
        print('Service ready to compute!')
	rospy.spin()   #prevent from dying

if __name__ == '__main__':
	compute_cubic_coeffs()
