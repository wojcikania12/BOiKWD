#Anna Wójcik
import numpy as np
from scipy.optimize import linprog


macierz = np.array([[0, 2, -3, 0],
                    [-2, 0, 0, 3],
                    [3, 0, 0, -4],
                    [0, -3, 4, 0]])


'''          (1,1) (1,2) (2,1) (2,2)
(1,1)         0     2     −3     0
(1,2)         −2    0      0     3
(2,1)         3     0      0    −4
(2,2)         0    −3      4     0
--------------------------------------
(i,j) i - ilość pokazanych palców, j - odgadnięcie ile palców przeciwnik pokaże

'''
min =  abs(macierz.min())
macierz = macierz + min

a = [1, 1, 1, 1]
b = [-1, -1, -1, -1]


min_m = - macierz
macierz1 = np.transpose(min_m)
wartosci1 = linprog(a,macierz1,b)
wartosc_gry1 = 1.0/np.sum(wartosci1.x)
wynik1 = wartosci1.x * wartosc_gry1



print("-------------------Gracz 1------------------ ")
print("Prawdopodobieństwo: p1 = {0}   p2 = {1}  p3 = {2}   p4 = {3} \nWartość gry : {4}\n".format(round(wynik1[0],2),round(wynik1[1],2),round(wynik1[2],2),round(wynik1[3],2),abs(round(wartosc_gry1 - min,2))))

