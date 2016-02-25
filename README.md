# pioneer3at_navigator
Pioneer 3AT Robot Autonomous Navigator

#### 1. Install RosAria to provide an interface to the Pioneer3at robot. 
Source: `http://wiki.ros.org/ROSARIA/Tutorials/How%20to%20use%20ROSARIA`

1. `cd ~/catkin_ws/src`
2. `git clone https://github.com/amor-ros-pkg/rosaria.git`
3. `cd ..`
4. `rosdep update`
5. `rosdep install rosaria`
6. `catkin_make`
7. `sudo apt-get install ros-indigo-move-base ros-indigo-turtlebot-teleop ros-indigo-map-server ros-indigo-robot-localization ros-indigo-amcl`
8. `rospack profile`

#### 2. Use UDEV rules to create a device alias for Pioneer3At. 
Source: `http://www.reactivated.net/writing_udev_rules.html`

1. Find the vendor_id and product_id of the usb to serial adapter
2. `sudo lsusb`
3. Returned: Bus 002 Device 014: ID 067b:2303 Prolific Technology, Inc. PL2303 Serial Port
4. Vendor_ID:067b and Product_ID:2303, use these in #6 below.
5. `sudo su`
6. `echo 'SUBSYSTEM=="tty", ATTRS{idVendor}=="067b", ATTRS{idProduct}=="2303", SYMLINK+="pioneer", GROUP="dialout", MODE="0660"' >> /etc/udev/rules.d/99-pioneer.rules`
7. `sudo udevadm control --reload-rules`
8. Unplug usb cable to pioneer3at and replug it in.

#### 3. Test the pioneer3at install
1. `roslaunch pioneer3at_navigator teleop_only.launch`
2. While holding in the left bumper button on xbox controller, move the left joystick to drive the robot.

#### 4. Install p2os_urdf. On 25JAN2016 p2os_urdf was unavailable thru apt-get.
1. Locate the file: p2os_urdf.tar.gz in the pioneer3at_navigator src directory.
2. Extract this file into ~/catkin_ws/src/
3. `cd ~/catkin_ws`
4. `catkin_make`

#### 5. Install the velodyne laser packages.
Use the instruciont found at https://github.com/westpoint-robotics/usma_velodyne.git.
    
#### 6. Install umsa_xsens if using the xsens IMU/GPS. 
Use the instruciont found at https://github.com/westpoint-robotics/usma_xsens.git.

#### 7. Test the install of usma_xsens.
use: `roslaunch xsens_driver xsens_driver.launch`

## Running the package
use: `roslaunch pioneer3at_navigator autonomous.launch` 

