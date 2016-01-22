# pioneer3at_navigator
Pioneer 3AT Robot Autonomous Navigator


## Velodyne VLP-16 Laser Ros Driver support:
Do not install the velodyne driver from the ros repository. The latest master branch on github is required for the VLP-16 support. Clone the repo from https://github.com/westpoint-robotics/pioneer3at_navigator.git to catkin_ws/src. 

## XSens IMU support
Use the XSens driver from West Point Robitics at https://github.com/westpoint-robotics/usma_xsens.git. This has the support for the newer protocol used.

## Running the package
use:
roslaunch pioneer3at_navigator autonomous.launch 
