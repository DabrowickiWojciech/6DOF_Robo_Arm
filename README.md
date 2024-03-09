# 6 DOF Robo Arm
The project only has program without any mechanical parts.

## Table of contents
- [About The Project](#about-the-project)
    - [Code](#code)
        - [arm_1.1.py](#arm_1.1.py)
        - [rearranged](#rearranged.py)

## About The Project
I was encourage to take part in a uni project that was a 6 degrees of freedom robo arm. The code included has 2 parts.
Code:
/src/arm_1.1.py
/src/rearanged.py
Info:
This part is just to simplify what should you have before coding (jpg) and matlab file was made to help with matrixes.

## Code
#### arm_1.1.py
Within the folder src there are two files, first arm1.1.py contains only forward kinematics, but it's universal for all robo arms. Therefor it's not optimized.
Array A06 is a forward kinematics matrix and simplest inverse kinematics.

#### rearranged.py
Second updated file that provides more complex solution for inverse kinematics and optimized forward kinematics created using:

<p align="center" width="100%">
    <img src="info/Axis_rotations.jpg">
</p>