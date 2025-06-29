# 5 DOF Robot Arm Simulations

This repository contains a simple Gazebo/ROS simulation of a five degree-of-freedom robotic arm. The launch files run either an RViz visualization or spawn the robot in an empty Gazebo world.

## Installation Prerequisites

- **ROS Noetic** (Ubuntu 20.04) with the `gazebo_ros` packages
- **Gazebo 11** (installed alongside ROS Noetic)

Ensure that you have a working [catkin](http://wiki.ros.org/catkin) workspace. Clone this repository into the `src` folder of your workspace and build it using `catkin_make`.

```bash
cd ~/catkin_ws/src
git clone <this repository> robo_arm_3
cd ..
catkin_make
```

## Quick Start

After building the workspace, source it and run one of the provided launch files.

### RViz display

```bash
source ~/catkin_ws/devel/setup.bash
roslaunch robo_arm_3 display.launch
```

This opens RViz with the robot description loaded so you can manipulate the joints using the GUI sliders.

### Gazebo simulation

```bash
source ~/catkin_ws/devel/setup.bash
roslaunch robo_arm_3 gazebo1.launch
```

This spawns the arm in an empty Gazebo world and loads the effort controllers defined in `config/joint_state_controller.yaml`. `rqt_reconfigure` and `rqt_publisher` are started automatically for quick testing.

## Scripts Overview

The `scripts/` directory contains a few Python helpers used while developing the arm model:

- **`dh_mat_sym.py`** – Builds Denavit‑Hartenberg transformation matrices with **sympy** for the arm and provides the symbolic forward kinematics.
- **`ik_new.py`** – Demonstrates solving the inverse kinematics for a single desired pose using trigonometric equations and the symbolic matrices.
- **`jacobian.py`** – Implements the `JacobinaMatrix` class to compute the manipulator Jacobian and its inverse when the determinant is sufficiently large.
- **`straight_line.py`** – Example of using the Jacobian inverse to follow a straight‑line Cartesian trajectory by iteratively updating the joint angles.

These scripts are not integrated with the launch files but serve as examples of analytical computations for the arm.
