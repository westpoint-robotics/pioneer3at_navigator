# pioneer3at_navigator
Pioneer 3AT Robot Autonomous Navigator

#### 1. Install RosAria to provide an interface to the Pioneer3at robot. 
    (from: http://wiki.ros.org/ROSARIA/Tutorials/How%20to%20use%20ROSARIA)
    1. cd ~/catkin_ws/src
    2. git clone https://github.com/amor-ros-pkg/rosaria.git
    3. cd ..
    4. rosdep update
    5. rosdep install rosaria
    6. catkin_make
    7. sudo apt-get install ros-indigo-move-base ros-indigo-turtlebot-teleop ros-indigo-map-server ros-indigo-robot-localization ros-indigo-amcl
    8. rospack profile

#### 2. Use UDEV rules to create a device alias for Pioneer3At. 
    (http://www.reactivated.net/writing_udev_rules.html)
    1. # find the vendor_id and product_id of the usb to serial adapter
    2. sudo lsusb
    3. # Returned: Bus 002 Device 014: ID 067b:2303 Prolific Technology, Inc. PL2303 Serial Port
    4. # Vendor_ID:067b and Product_ID:2303, use these in #6 below.
    5. sudo su
    6. echo 'SUBSYSTEM=="tty", ATTRS{idVendor}=="067b", ATTRS{idProduct}=="2303", SYMLINK+="pioneer3at", GROUP="dialout", MODE="0660"' >> /etc/udev/rules.d/99-pioneer.rules
    7. sudo udevadm control --reload-rules
    8. # unplug usb cable to pioneer3at and replug it in.
    
#### 3. Test the pioneer3at install
    1. roslaunch pioneer3at_navigator teleop_only.launch 
    2. # while holding in the left bumper button on xbox controller, move the left joystick to drive the robot.
    
#### 4. Install p2os_urdf. On 25JAN2016 p2os_urdf was unavailable thru apt-get.
    1. # Locate the file: p2os_urdf.tar.gz in the pioneer3at_navigator src directory.
    2. # Extract this file into ~/catkin_ws/src/
    3. cd ~/catkin_ws
    4. catkin_make 

#### 5. Install the velodyne laser packages from github.
    1. cd ~/catkin_ws/src
    2. git clone https://github.com/ros-drivers/velodyne.git
    3. cd ~/catkin_make
    4. catkin_make

#### 6. Make a network connection for the velodyne VLP16.
    1. sudo chown root:root velodyneVLP16
    2. sudo chmod 600 velodyneVLP16
    3. sudo cp velodyneVLP16 /etc/NetworkManager/system-connections/
    4. sudo service network-manager restart
    5. # In the network-manager gui, connect to velodyneVLP16 
    
#### 7. Install umsa_xsens if using the xsens IMU/GPS. 
    1. cd ~/catkin_ws/src
    2. git clone https://github.com/westpoint-robotics/usma_xsens.git
    3. sudo apt-get install ros-indigo-gps-common libpcap0.8-dev
    4. sudo su
    5. echo 'SUBSYSTEM=="tty", ATTRS{idVendor}=="2639", ATTRS{manufacturer}=="Xsens", ATTRS{product}=="MTi-G-700 GPS/INS", ACTION=="add", GROUP="dialout", MODE="0660"' >> /etc/udev/rules.d/99-xsens.rules
    6. exit
    7. cd ~/catkin_make
    8. catkin_make

#### 8. Test the install of usma_xsens.
    1. roslaunch xsens_driver xsens_driver.launch 

## Running the package
use:
roslaunch pioneer3at_navigator autonomous.launch 

## Velodyne VLP-16 Laser Ros Driver support:
Do not install the velodyne driver from the ros repository. The latest master branch on github is required for the VLP-16 support. Clone the repo from https://github.com/westpoint-robotics/pioneer3at_navigator.git to catkin_ws/src. 

## XSens IMU support
Use the XSens driver from West Point Robitics at https://github.com/westpoint-robotics/usma_xsens.git. This has the support for the newer protocol used.

## Running the package
use:
roslaunch pioneer3at_navigator autonomous.launch 
