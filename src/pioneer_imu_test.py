#!/usr/bin/env python  

import roslib
import rospy
import sys
import time
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseWithCovarianceStamped
from move_base_msgs.msg import MoveBaseActionGoal

pub = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=1)
#pub = rospy.Publisher('/move_base/goal', MoveBaseActionGoal, queue_size=5)
if len(sys.argv) == 3:
    delta_x = sys.argv[1]
    delta_y = sys.argv[2]
elif len(sys.argv) == 2:
    delta_x = sys.argv[1]
    delta_y = 0
else:
    delta_x = 1
    delta_y = -0.4

global sub_once
global goal_pose
goal_pose=PoseStamped()

def odom_callback(data):

    goal_pose.header.frame_id = 'map'
    goal_pose.header.stamp = data.header.stamp
    goal_pose.pose.position.x = data.pose.pose.position.x + delta_x
    goal_pose.pose.position.y = data.pose.pose.position.y + delta_y    
    goal_pose.pose.orientation = data.pose.pose.orientation
    str = "\nMoving from ({0},{1})  to goal of ({2},{3})".format(data.pose.pose.position.x,data.pose.pose.position.y,goal_pose.pose.position.x, goal_pose.pose.position.y )
    rospy.loginfo(str)
    sub_once.unregister()
    #rospy.signal_shutdown("Published a goal")

if __name__ == '__main__':
    rospy.init_node('simple_goal_Py', anonymous=True)
    sub_once=rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, odom_callback)
    #sub_once=rospy.Subscriber('/odom', Odometry, odom_callback)
    rate = rospy.Rate(2) # 10hz
    while not rospy.is_shutdown():
        pub.publish(goal_pose)
        rate.sleep()
    




