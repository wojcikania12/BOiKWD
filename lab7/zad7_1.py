#Anna Wójcik
from scipy.optimize import linprog

A = [[1, 1, 1],
     [-1, -1, -1],
     [-1, -2, -1],
     [0, 2, 1]]

b = [30, -30, -10, 20]

f = [-2, -1, -3]

wynik =  linprog(f, A, b)
tablica_wynikow=  wynik.x

print("Rozwiązanie:\nx1 = {0} ≈ {1}\nx2 = {2} ≈ {3}\nx3 = {4} ≈ {5}".format(tablica_wynikow[0],round(tablica_wynikow[0]),
                                                                            tablica_wynikow[1],round(tablica_wynikow[1]),
                                                                            tablica_wynikow[2],round(tablica_wynikow[2])))


#  x1+x2+x3=30  zmieniamy w  parę  x1+x2+x3<=30 i -x1 -x2-x3<=-30
#  x1+2x2+x3>=10 zmieniamy w -x1-2*x2-x3<=-10
#   2*x2+x3<=20 zostawiamy
