# KUKA LWR 4+ manipulator URDF model
<img src="https://img.shields.io/badge/ros--version-humble-green"/>  <img src="https://img.shields.io/badge/platform%20-Ubuntu%2022.04-orange"/>

## Description :clipboard: 

The `lwr_description` package contains an URDF model of the 7-DOF **KUKA LWR 4+** manipulator. A parameterized launch file was added to run the entire visualization. The shape of the manipulator was described by CAD files in COLLADA format (_.dae_), instead of geometric primitives, to mimic the real manipulator.

<p align="center">
<img src="https://user-images.githubusercontent.com/80155305/236012652-7ee8ad62-859a-434a-9ada-c28944b451d3.png" width="500" height="350"/>
</p> 


## Installation :arrow_down:

It is recommended to use Ubuntu 22.04 with [**ROS 2 Humble**](https://docs.ros.org/en/humble/index.html). There are 3 versions of ROS2 Humble Hawksbill to choose from: Desktop Install, ROS-Base Install and Development tools Install. Be sure to install **Desktop Install** version, because it includes GUI tools such as RViz.

### Required packages
Packages such as **joint_state_publisher, joint_state_publisher_gui, robot_state_publisher, rviz2** and **xacro** are required to run the visualization. You can install them all at once using the `sudo apt install ros-humble-urdf-tutorial` command. 
  
  
### Building from source

```
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/
git clone https://github.com/jkaniuka/kuka_lwr4plus_urdf.git -b ros2 src/
source /opt/ros/humble/setup.bash
colcon build
. install/setup.bash
```

## Running :arrow_forward:
The command below will start the visualization and `joint_state_publisher_gui` node, which will allow you to control the manipulator.
```
ros2 launch lwr_description display.launch.py 
```

If you want to write a custom node to control the manipulator by publishing messages on the _/joint\_states_ topic, run the visualization without `joint_state_publisher_gui`. You can do this by setting the `use_gui` argument to `false` (see below).

```
ros2 launch lwr_description display.launch.py use_gui:=false
```
