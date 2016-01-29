#!/usr/bin/env python  

import roslib
import rospy
import sys
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseWithCovarianceStamped

pub = rospy.Publisher('/test/goal', PoseStamped, queue_size=1)
delta_x = 1
delta_y = 1
global sub_once
def odom_callback(data):
    goal_pose=PoseStamped()
    goal_pose.pose.position.x = data.pose.pose.position.x + delta_x
    goal_pose.pose.position.y = data.pose.pose.position.y + delta_y    
    goal_pose.pose.orientation = data.pose.pose.orientation
    pub.publish(goal_pose)
    str = "Moving  to goal of ({0},{1})" .format(goal_pose.pose.position.x, goal_pose.pose.position.y)
    rospy.loginfo(str)
    sub_once.unregister()
    sys.exit(1)

if __name__ == '__main__':
    rospy.init_node('simple_goal_Py', anonymous=True)

    sub_once=rospy.Subscriber('/robot_pose_ekf/odom_combined', PoseWithCovarianceStamped, odom_callback)
    rospy.spin()

