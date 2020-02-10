#Anna Wójcik

from scipy.optimize import linprog
import numpy as np


b = [-12000, -18000]
A = [[4,1,8,5,2,0],
     [0,1,0,1,2,3]]
f = [0.1,0.2,0.2,0.3,0.4,0]

A_transpose = np.transpose(A)

y = linprog(b, A_transpose,  f)
tablica_y=  y.x

b = [12000, 18000]
A = [[4,0,8,0,0,0],
     [0,0,0,0,0,3]]


x6 = 18000 / 3

print('y1: ',np.round(tablica_y[0],3), ' y2: ',np.round(tablica_y[1],2))
print('x1 + 2x3 = 3000   x6: ',x6)
print('Należy 6000 razy pociąć balę 4,2 m  3 razy po 1,4 m. Natomiast ilość pociętych bal 2,1 m 4 razy po 0,5m jak '
      'i tych 4,2 m  8 razy po 0,5 m jest od siebie zależna. Suma tych dwóch rodzajów cięć ma dać 3000. ')



'''
model problemu
4x1 + x2 + 8x3 + 5x4 + 2x5 >= 12000
x2 + x4 + 2x5 + x6 >= 18000
x1, ...., x6 >= 0
 
0,1x1 + 0,2x2 + 0,2x3 + 0,3x4 + 0,4x5 + 0x6 -> min
 
postać dualna:
 
4y1 <= 0.1
y1+ y2 <= 0.2 -> ostro spełniony, x2 = 0
8y1 <= 0.2
5y1+ y2 <= 0.3 -> ostro spełniony, x4 = 0
2y1+ 2y2 <= 0.4 -> ostro spełniony, x5 = 0
y2 <= 0
 
12 000y1 + 18 000y2 -> max
 
y1 = 0.025 / y2 = 0
 
po zredukowaniu:

4x1 + 8x3  = 12000
3x6 = 18000
 
'''