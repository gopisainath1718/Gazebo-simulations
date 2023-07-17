#!usr/bin/env python3
import sympy as sp
import numpy as np

t_1, t_2, t_3, t_4, t_5 = sp.symbols('t_1, t_2, t_3, t_4, t_5')

#dimensions in mm
theta = [0*(np.pi/180), t_1*(np.pi/180), t_2*(np.pi/180), t_3*(np.pi/180), (90+t_4)*(np.pi/180), t_5*(np.pi/180)]
d = [40, 60, 0, 0, 64.416, 193.721]
a = [0, 0, 383.48, 273.14, 0, 0]
alpha = [0*(np.pi/180), 90*(np.pi/180), 0*(np.pi/180), 0*(np.pi/180), 90*(np.pi/180),0*(np.pi/180)]

# theta = [t_1*(np.pi/180), t_2*(np.pi/180), t_3*(np.pi/180)]
# d = [60, 0, 0]
# a = [0, 383.48, 273.14]
# alpha = [90*(np.pi/180), 0*(np.pi/180), 0*(np.pi/180)]

def tf_mat_sym(i):
    m =[[sp.cos(theta[i]), -sp.sin(theta[i])*sp.cos(alpha[i]), sp.sin(theta[i])*sp.sin(alpha[i]) , a[i]*sp.cos(theta[i])],
        [sp.sin(theta[i]), sp.cos(theta[i])*sp.cos(alpha[i]) , -sp.cos(theta[i])*sp.sin(alpha[i]), a[i]*sp.sin(theta[i])],
        [0               , np.sin(alpha[i])                  , sp.cos(alpha[i])                  , d[i]                 ],
        [0               , 0                                 , 0                                 , 1                    ]]

    return sp.Matrix(m)

matrix_sym = sp.sympify(tf_mat_sym(0)*tf_mat_sym(1)*tf_mat_sym(2)*tf_mat_sym(3)*tf_mat_sym(4)*tf_mat_sym(5))
# matrix_sym = sp.sympify(tf_mat_sym(0)*tf_mat_sym(1)*tf_mat_sym(2))

t07 = matrix_sym.evalf(subs={t_1:0, t_2:0, t_3:-20, t_4:0, t_5:0})
#print(matrix_sym[1 ,0])
#print("\n")
#print(sp.Matrix(t07))

