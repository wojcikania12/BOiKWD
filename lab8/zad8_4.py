# Anna Wójcik

from scipy.optimize import linprog
import numpy as np


A = [[1, 2, 0, 0, 0, 2, 0, 1, 1], [-1, -2, 0, 0, 0, -2, 0, -1, -1], [1, 1, 2, 1, 0, 0, 3, 2, 0],
     [-1, -1, -2, -1, 0, 0, -3, -2, 0], [2, 0, 2, 4, 6, 1, 1, 0, 3], [-2, 0, -2, -4, -6, -1, -1, 0, -3]]
b = [12000, -12000, 24000, -24000, 27000, -27000]

f = [1, 0, 4, 2, 0, 3, 1, 3, 4]

wynik = linprog(f, A, b)
print(np.round(wynik.x,2))

print('Należy pociąć:\n6000 kawałków - 2 gwoździe 11cm i 1 gwóźdź 8cm\n6000 kawałków '
      '- 3 gwoździe 8cm i 1 gwóźdź 5cm\n3500 kawałków - 6 gwoździ 5cm ')

'''
model problemu
x1+2x2+2x6+x8+x9 = 12000
x1+x2+2x3+x4+3x7+2x8 = 24000
2x1+2x3+4x4+6x5+x6+x7+2x8+3x9 = 27000

x1+0x2+4x3+2x4+0x5+3x6+x7+3x8+4x9 -> min
  
x1) 11cm + 8cm + 2 po 5 cm
x2) 2 po 11 cm + 8 cm
x3) 2 po 8cm + 2 po 5 cm
x4) 8cm + 4 po 5 cm
x5) 6 po 5cm
x6) 2 po 11cm + 5cm
x7) 3 po 8 cm + 5cm
x8) 11cm + 2 po 8cm
x9) 11cm + 3 po 5cm

'''