#Anna Wójcik
from scipy.optimize import linprog

A = [[-5, -15],
     [-20 ,-5],
     [15, 2]]

b = [-50, -40, 60]

f = [8, 4]

wynik =  linprog(f, A, b)
tablica_wynikow=  wynik.x

print("Rozwiązanie:\nx1 = {0} ≈ {1}\nx2 = {2} ≈ {3}".format(tablica_wynikow[0],round(tablica_wynikow[0],2),
                                                                            tablica_wynikow[1],round(tablica_wynikow[1],2)))

