#!/usr/bin/env python  

import roslib
import rospy
import sys
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseWithCovarianceStamped

print len(sys.argv)
pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=5)
if len(sys.argv) == 3:
    delta_x = sys.argv[1]
    delta_y = sys.argv[2]
elif len(sys.argv) == 2:
    delta_x = sys.argv[1]
    delta_y = 0
else:
    delta_x = 1
    delta_y = 0

global sub_once

def odom_callback(data):
    goal_pose=PoseStamped()
    goal_pose.header.frame_id = 'map'
    goal_pose.header.stamp = data.header.stamp
    goal_pose.pose.position.x = data.pose.pose.position.x + delta_x
    goal_pose.pose.position.y = data.pose.pose.position.y + delta_y    
    goal_pose.pose.orientation = data.pose.pose.orientation
    pub.publish(goal_pose)
    str = "\nMoving from ({0},{1})  to goal of ({2},{3})".format(data.pose.pose.position.x,data.pose.pose.position.y,goal_pose.pose.position.x, goal_pose.pose.position.y )
    rospy.loginfo(str)
    #sub_once.unregister()
    #rospy.signal_shutdown("Published a goal")

if __name__ == '__main__':
    rospy.init_node('simple_goal_Py', anonymous=True)
    #sub_once=rospy.Subscriber('/robot_pose_ekf/odom_combined', PoseWithCovarianceStamped, odom_callback)
    sub_once=rospy.Subscriber('/odom', Odometry, odom_callback)
    rospy.spin()

