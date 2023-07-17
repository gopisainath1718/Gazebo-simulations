from jacobian import JacobinaMatrix
import sympy as sp
import dh_mat_sym as dh

jacobian1 = JacobinaMatrix()
sq_mat = jacobian1.jacobina_square_matrix(0, 70, -115, -40, 0)
# det = jacobian1.det(sq_mat)
inv_mat = jacobian1.inverse_jacobian(sq_mat)
print(inv_mat)


#                              dx   dy   dz  dwx  dwy
end_effector_vel = sp.Matrix([[1], [0], [0], [0], [0]])
# new_t_1, new_t_2, new_t_3, new_t_4, new_t_5 = dh.t_1, dh.t_2, w

# Finding joint angle velocitires
# j.jacobian_matrix = sp.Matrix(j.jacobian_matrix).subs({dh.t_1:0, dh.t_2:70, dh.t_3:-115, dh.t_4:-40, dh.t_5:0})
joint_angle_vel = sp.sympify(sp.Matrix(inv_mat[0])*end_effector_vel)
# print("\n")
# print(joint_angle_vel)

# time_step = 0.5
while inv_mat[1] >=10 :

    # new angles
    dt_2 = joint_angle_vel[1]*0.5
    dt_3 = joint_angle_vel[2]*0.5
    dt_4 = joint_angle_vel[3]*0.5

    new_t_2 = jacobian1.t2 + dt_2
    new_t_3 = jacobian1.t3 + dt_3
    new_t_4 = jacobian1.t4 + dt_4

    sq_mat = jacobian1.jacobina_square_matrix(0, new_t_2, new_t_3, new_t_4, 0)
    inv_mat = jacobian1.inverse_jacobian(sq_mat)
    joint_angle_vel = sp.sympify(sp.Matrix(inv_mat[0])*end_effector_vel)

    print("\n")
    print(f"new_t_2:{new_t_2}, new_t_3:{new_t_3}, new_t_4:{new_t_4}")

    

