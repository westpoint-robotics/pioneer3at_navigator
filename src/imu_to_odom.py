#!/usr/bin/env python
import roslib
import rospy
import time
from sensor_msgs.msg import Imu 
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose

class Imu2Odom:

    def __init__(self):
        rospy.init_node('imu_to_odom')
        self.pub = rospy.Publisher('/imu/odom', Odometry, queue_size=1)
        self.sub = rospy.Subscriber("imu/data", Imu, self.handle_imu)
        
        self.imu_recv = False
        rospy.loginfo('IMU2Odom initialized.')
        
        rospy.spin()

    def handle_imu(self, imu_data):
        
        if not self.imu_recv:
            
            rospy.loginfo('IMU data received')
            self.imu_recv = True
    
        if self.pub.get_num_connections() != 0:
    
          msg = Odometry()
          
          #msg.header.frame_id = imu_data.header.frame_id
          msg.header.frame_id = 'imu_frame'
          msg.header.stamp = imu_data.header.stamp
          
          msg.child_frame_id = 'imu_base_link'
          
          msg.pose.pose.position.x = 0.0 # here, we can maybe try to integrate accelerations...
          msg.pose.pose.position.y = 0.0
          msg.pose.pose.position.z = 0.0
          
          msg.pose.pose.orientation = imu_data.orientation # should we transform this orientation into base_footprint frame????
          
          msg.pose.covariance = [99999, 0,     0,     0,     0,     0, # large covariance on x, y, z
                                 0,     99999, 0,     0,     0,     0,
                                 0,     0,     99999, 0,     0,     0, 
                                 0,     0,     0,     1e-06, 0,     0, # we trust in rpy
                                 0,     0,     0,     0,     1e-06, 0,
                                 0,     0,     0,     0,     0,     1e-06]
          
          # does robot_pose_ekf care about twist?
          
          self.pub.publish(msg)
          

if __name__ == '__main__':
    imu2dom = Imu2Odom()
