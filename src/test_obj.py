#!/usr/bin/env python  

import roslib
import rospy
import sys
import time
from visualization_msgs.msg import Marker

print len(sys.argv)
vPub = rospy.Publisher('visualization_marker',Marker, queue_size=1)


if len(sys.argv) == 3:
    delta_x = sys.argv[1]
    delta_y = sys.argv[2]
elif len(sys.argv) == 2:
    delta_x = sys.argv[1]
    delta_y = 0
else:
    delta_x = 0
    delta_y = 1

if __name__ == '__main__':
    rospy.init_node('viz_obj', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    marker = Marker()
    marker.header.frame_id = "map"
    #marker.header.stamp = rospy.Time.now()
    marker.ns = "namespace"
    marker.id = 0
    marker.type = Marker.SPHERE
    marker.action = Marker.ADD
    marker.pose.position.x = 0
    marker.pose.position.y = 0
    marker.pose.position.z = 1
    marker.pose.orientation.x = 0.0
    marker.pose.orientation.y = 0.0
    marker.pose.orientation.z = 0.0
    marker.pose.orientation.w = 1.0
    marker.scale.x = 0.1
    marker.scale.y = 0.1
    marker.scale.z = 0.1
    marker.color.a = 1.0 
    marker.color.r = 0.0
    marker.color.g = 1.0
    marker.color.b = 0.0
    marker.lifetime.secs = 120
    marker.mesh_resource = "/opt/ros/indigo/share/pr2_description/meshes/base_v0/base.dae"
    while not rospy.is_shutdown():
        vPub.publish( marker )
        rate.sleep()

    




