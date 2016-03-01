#!/usr/bin/env python

""" Code modified by: Dominic Larkin 5FEB2016

    This code combines an IMU message with a Odom message.

    I puts the orientation of the IMU at the X an Y coordinate of the outMsg.
"""
#!/usr/bin/python
import time
import serial
import rospy
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu


p3AtPose = Odometry()
imuData = Imu()

def update_imu(data):
    global imuData
    imuData=data

def update_pose(data):
    global p3AtPose
    p3AtPose=data

# Start the ROS node and create the ROS publisher and subscribers   
gpsPub = rospy.Publisher('odomIMu', Odometry, queue_size=1)
rospy.Subscriber('/imu/data', Imu, update_imu)
rospy.Subscriber('/RosAria/pose', Odometry, update_pose)

rospy.init_node('imu_on_odom', anonymous=True)
rate = rospy.Rate(30)


try:
    while not rospy.is_shutdown(): 
        outMsg = Odometry()
        outMsg.header.stamp = imuData.header.stamp;
        outMsg.header.frame_id = "map";

        #set the position
        outMsg.pose.pose.position= p3AtPose.pose.pose.position
        outMsg.pose.pose.orientation = imuData.orientation

        #set the twist
        outMsg.child_frame_id = "imu_base";
        #outMsg.twist.twist.linear.x = imuTwist.vx;
        #outMsg.twist.twist.linear.y = imuTwist.vy;
        #outMsg.twist.twist.angular.z = imuData.angular_velocity.z
        gpsPub.publish(outMsg)
                  
except KeyboardInterrupt:
    raise

'''
rosmsg show nav_msgs/Odometry

std_msgs/Header header
  uint32 seq
  time stamp
  string frame_id
string child_frame_id
geometry_msgs/PoseWithCovariance pose
  geometry_msgs/Pose pose
    geometry_msgs/Point position
      float64 x
      float64 y
      float64 z
    geometry_msgs/Quaternion orientation
      float64 x
      float64 y
      float64 z
      float64 w
  float64[36] covariance
geometry_msgs/TwistWithCovariance twist
  geometry_msgs/Twist twist
    geometry_msgs/Vector3 linear
      float64 x
      float64 y
      float64 z
    geometry_msgs/Vector3 angular
      float64 x
      float64 y
      float64 z
  float64[36] covariance

rosmsg show sensor_msgs/Imu
std_msgs/Header header
  uint32 seq
  time stamp
  string frame_id
geometry_msgs/Quaternion orientation
  float64 x
  float64 y
  float64 z
  float64 w
float64[9] orientation_covariance
geometry_msgs/Vector3 angular_velocity
  float64 x
  float64 y
  float64 z
float64[9] angular_velocity_covariance
geometry_msgs/Vector3 linear_acceleration
  float64 x
  float64 y
  float64 z
float64[9] linear_acceleration_covariance

'''
