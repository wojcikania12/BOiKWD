#Anna Wójcik

from scipy.optimize import linprog
import numpy as np

A = [[1, 3, 2, 3, 1],
     [4, 6, 5, 7, 1]]

b = [6,15]

f = [-2, -5, -3, -4, -1]

A_transpose = -(np.transpose(A))

y = linprog(b, A_transpose,  f)
tablica_y=  y.x
print('y1: ',np.round(tablica_y[0],3), ' y2: ',np.round(tablica_y[1],2))

A =[[1 , 3],[4,6]]
b = [6,15]

wynik = np.linalg.solve(A,b)
print('x1: ',np.round(wynik[0],3), ' x2: ',np.round(wynik[1],3))
'''
model problemu
x1 + 3x2 +2x3 + 3x4 + x5 <= 6
4x1 + 6x2 +5x3 + 7x4 + x5 <= 15

x1, ...., x5 >= 0
2x1 + 5x2 + 3x3 + 4x4 + x5  -> max

postać dualna:

y1+ 4y2 >= 2 
3y1+ 6y2 >= 5 
2y1 + 5y2 >= 3 -> ostro spełniony, x3 = 0
3y1+ 7y2 >= 4 -> ostro spełniony, x4 = 0
y1+ y2 >= 1  -> ostro spełniony, x5 = 0

6y1 + 15y2 -> min

y1 = 1.33 / y2 = 0.17

po zredukowaniu:
x1 + 3x2  = 6
4x1 + 6x2 = 15

'''
