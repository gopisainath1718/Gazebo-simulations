from math import acos, asin, atan, cos, pi, sqrt
import numpy as np
import sympy as sp
import dh_mat_sym as dh
desired_pose =[[0.342020143325669, -5.75395780113925e-17, 0.939692620785908, 822.185836632730], [5.75395780113925e-17, -1.00000000000000, -8.21750336457526e-17, -64.4160000000000], [0.939692620785908, 8.21750336457526e-17, -0.342020143325669, -59.6758661331650], [0, 0, 0, 1.00000000000000]]

t4, t5 = sp.symbols('t4, t5')

#a = [0, 0, 383.48, 273.14, 0, 0, 0]
a1, a2, a3, a4, a5, a6 = 0, 0, 383.48, 273.14, 0, 0
#d = [40, 60, 0, 0, 64.416, 93.721, 100]
d1, d2, d3, d4, d5, d6 = 40, 60, 0, 0, 64.416, 193.721

gripper_centre = [[desired_pose[0][3] - d6*desired_pose[0][2]],
                  [desired_pose[1][3] - d6*desired_pose[1][2]],
                  [desired_pose[2][3] - d6*desired_pose[2][2]]]
#print(gripper_centre)                  

#Finding t1
r =sqrt((gripper_centre[0][0]**2)+(gripper_centre[1][0]**2))
offset_angle = asin(64.416/r)
#print(offset_angle)
original_angle = atan(gripper_centre[1][0]/gripper_centre[0][0])
if gripper_centre[0][0]<0:
    original_angle = original_angle +3.141592654
t1 = (offset_angle + original_angle)*180/np.pi
print("t1: ",t1)


#Finding t2
z = gripper_centre[2][0] - (d1 + d2)
temp = gripper_centre[0][0]**2 + gripper_centre[1][0]**2
l1 = sqrt((temp) + (z**2))
angle1 = acos((a3**2 + l1**2 - a4**2) / (2*a3*l1)) #rad
angle2 = atan(z/sqrt(temp))
t2 = angle1 + angle2
print("t2: ", t2*180/pi)

#Finding t3
angle3 = acos((a4**2 + a3**2 - l1**2) / (2*a4*a3))
t3 = -(pi - angle3)
print("t3: ", t3*180/pi)

#Finding t4, t5

t04 = sp.sympify(dh.tf_mat_sym(0)*dh.tf_mat_sym(1)*dh.tf_mat_sym(2)*dh.tf_mat_sym(3))
g= t04.evalf(subs={dh.t_1:t1, dh.t_2:t2, dh.t_3:t3})
t04_f = g[0:3, 0:3]
t04_T = t04_f.T
d_p = np.array(desired_pose)
R_f = t04_T*d_p[0:3, 0:3]

t46 = sp.sympify(dh.tf_mat_sym(4)*dh.tf_mat_sym(5))

t46_f = t46[0:3, 0:3]
#print(t46_f)
t5 = asin(R_f[2, 0])

#t4 = atan(R_f[1, 0] / R_f[0, 0]) - 1.5707963267949
t4 = -acos((R_f[0, 0]) / (cos(t5))) -1.5707963267949
t4_1 = asin(-R_f[0, 0]/cos(t5))
t4_2 = asin(R_f[0, 2]) - 1.5707963267949
t4_3 = atan(R_f[1, 0]/R_f[0, 0]) -1.5707963267949
#t5 = atan(R_f[0,2]/R_f[1, 2]) - 1.5707963267949
#t6 = acos(R_f[1, 2]) - 1.5707963267949

print("t4: ",t4*180/pi)
print("t4_1: ",t4_1*180/pi)
print("t4_2: ",t4_2*180/pi)
print("t4_3: ",t4_3*180/pi)
print("t5: ",t5*180/pi)
