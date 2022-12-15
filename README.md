### Garbage Cleaning Robot
## Overview

There is the final project for ENPM662 course where the custom designed robot moves in the gazebo world and performs the pick and place operation.

## Build/run steps

Create and go to the root of the workspace "catkin_ws" then type the following in the terminal: -

```
mkdir catkin_ws/src
cd ~/catkin_ws/src
unzip the file "manipulator.zip"
cd .. 
source /opt/ros/noetic/setup.bash
catkin_make
. devel/setup.bash
roslaunch manipulator template_launch.launch
```

Open another terminal 
```
cd ~/catkin_ws/
source /opt/ros/noetic/setup.bash
. devel/setup.bash
rosrun manipulator publisher_straight_line.py
```

## Dependencies
- ROS1 Noetic: 
To install the ROS - Noetic type the following command in the terminal:

```` 
http://wiki.ros.org/noetic/Installation/Ubuntu
````

- Required ROS Controllers installation:
```` 
ros-noetic-gazebo-ros-control 
````

- Python3
To install the python 3 type the following command in the terminal:

```` 
$ sudo apt-get install python3
````

- Gazebo (Will be installed along with ROS Noetic, if not use the below link to install):

```` 
sudo apt-get install gazebo11 ros-noetic-gazebo-ros  
````
