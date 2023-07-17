import numpy as np
import sympy as sp
import dh_mat_sym as dh

class JacobinaMatrix():

    end_position = sp.Matrix([[dh.matrix_sym[0, 3]], [dh.matrix_sym[1, 3]], [dh.matrix_sym[2, 3]]])

    linear_jacob = end_position.jacobian([dh.t_1, dh.t_2, dh.t_3, dh.t_4, dh.t_5])
    # # linear_jacob = linear_jacob.subs({dh.t_1:0, dh.t_2:0, dh.t_3:0, dh.t_4:0, dh.t_5:0})
    # # print(linear_jacob)

    tf_01 = dh.tf_mat_sym(0)
    rotational_jacob_1 = tf_01[0:3, 2]

    tf_02 = sp.sympify(tf_01*dh.tf_mat_sym(1))
    rotational_jacob_2 = tf_02[0:3, 2]

    tf_03 = sp.sympify(tf_02*dh.tf_mat_sym(2))
    rotational_jacob_3 = tf_03[0:3, 2]

    tf_04 = sp.sympify(tf_03*dh.tf_mat_sym(3))
    rotational_jacob_4 = tf_04[0:3, 2]

    tf_05 = sp.sympify(tf_04*dh.tf_mat_sym(4))
    rotational_jacob_5 = tf_05[0:3, 2]

    rotational_jacob =np.concatenate((rotational_jacob_1, rotational_jacob_2, rotational_jacob_3, rotational_jacob_4, rotational_jacob_5), axis=1)
    # # print(sp.Matrix(rotational_jacob))
    # # print("\n")
    jacobian_matrix = np.concatenate((linear_jacob, rotational_jacob), axis=0)

    def jacobina_square_matrix(self, t1, t2, t3, t4, t5):

        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t5 = t5
        
        jacobian_matrix = sp.Matrix(self.jacobian_matrix).subs({dh.t_1:t1, dh.t_2:t2, dh.t_3:t3, dh.t_4:t4, dh.t_5:t5})
        # # t_1 = 0, t_2 = 70, t_3 = -115, t_4 = -40, t_5 = 0
        # # print(sp.Matrix(jacobian_matrix))
        # # print(np.shape(jacobian_matrix))
        # # print("\n")

        # Jacobian Square Matrix
        jacobian_square_matrix = np.delete(jacobian_matrix, 5, 0)
        # # print("\n")
        return sp.Matrix(jacobian_square_matrix)
        # # print(np.shape(jacobian_square_matrix))
    
    # def det(self, mat):
    #     return sp.Matrix(mat).det()

    def inverse_jacobian(self, mat):

        det = sp.Matrix(mat).det()
        if det <=10:
            return "Inverse doesnt exist", det
        else:
            return sp.Matrix(mat).inv(), det

    
        

