#Anna Wójcik
import numpy as np
from scipy.optimize import linprog


macierz = np.array([[-2, 8, 2], [3, -1, 0]])
min =  abs(macierz.min())
macierz = macierz + min

a = [1,1]
b = [-1,-1,-1]

#gracz1
min_m = -macierz
macierz1 = np.transpose(min_m)
wartosci1 = linprog(a,macierz1,b)
wartosc_gry1 = 1.0/np.sum(wartosci1.x)
wynik1 = wartosci1.x * wartosc_gry1

#gracz2
wartosci = linprog(b,macierz,a)
wartosc_gry = 1.0/np.sum(wartosci.x)
wynik = wartosci.x * wartosc_gry


print("-------------------Gracz 1------------------ ")
print("Prawdopodobieństwo: p1 = {0}   p2 = {1}\nWartość gry : {2}\n".format(wynik1[0],wynik1[1],wartosc_gry1 - min))
print("-------------------Gracz 2------------------ ")
print("Prawdopodobieństwo: p1 = {0}   p2 = {1} p3 = {2}\nWartość gry : {3}".format(wynik[0],wynik[1],wynik[2],wartosc_gry - min))



