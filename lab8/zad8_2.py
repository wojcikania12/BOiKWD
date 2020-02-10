#Anna Wójcik

from scipy.optimize import linprog
import numpy as np

A = [[0.5, 0.4, 0.4, 0.2],
     [0.4, 0.2, 0, 0.5]]

b = [2000,2800]

f = [-10, -14, -8, -11]

A_transpose = -(np.transpose(A))

y = linprog(b, A_transpose,  f)
tablica_y=  y.x
print('y1: ',np.round(tablica_y[0],3), ' y2: ',np.round(tablica_y[1],2))

A =[[0.4 , 0.2],[0.2,0.5]]
b = [2000,2800]

wynik = np.linalg.solve(A,b)
print('x2: ',np.round(wynik[0],3), ' x4: ',np.round(wynik[1],3))
print('Produkcja 2750 sztuk produktu B i 4500 sztuk produktu D')

'''
model problemu
0,5x1 + 0,4x2 + 0,4x3 + 0,2x4  <= 2000
0,4x1 + 0,2x2  + 0,5x4 <= 2800

x1, ...., x4 >= 0
10x1 + 14x2 + 8x3 + 11x4  -> max

postać dualna:

0,5y1+ 0,4y2 >= 10 -> ostro spełniony, x1 = 0
0,4y1+ 0,2y2 >= 14
0,4y1>= 8 -> ostro spełniony, x3 = 0
0,2y1+ 0,5y2 >= 11 


2000y1 + 2800y2 -> min

y1 = 30 / y2 = 10

po zredukowaniu:

0,4x2 + 0,2x4  = 2000
0,2x2  + 0,5x4 = 2800
'''