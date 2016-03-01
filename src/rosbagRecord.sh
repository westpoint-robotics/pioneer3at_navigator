#!/bin/bash

rosbag record -O $HOME/catkin_ws/rosbags/pioneer/RosAria_cmd_vel.bag /RosAria/cmd_vel &
rosbag record -O $HOME/catkin_ws/rosbags/pioneer/RosAria_pose.bag /RosAria/pose &
rosbag record -O $HOME/catkin_ws/rosbags/pioneer/imu_data.bag /imu/data &
rosbag record -O $HOME/catkin_ws/rosbags/pioneer/pose2D.bag /pose2D &
rosbag record -O $HOME/catkin_ws/rosbags/pioneer/scan.bag /scan &
rosbag record -O $HOME/catkin_ws/rosbags/pioneer/tf.bag /tf &
rosbag record -a -O $HOME/catkin_ws/rosbags/pioneer/other.bag -x "/RosAria/cmd_vel|/RosAria/pose|/imu/data|/pose2D|/scan|/RosAria/sonar|/RosAria/sonar_pointcloud2|/velodyne*"
