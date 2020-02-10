#Anna Wójcik

from scipy.optimize import linprog

A = [[2,1], [1,1],[1,2.5] ,[-1, 0 ],[0, -1]]
b = [9000, 5500, 10000, -100, -100]
f = [-150/140, -130/250]
wynik = linprog(f,A, b,bounds =((0, None),(0 ,None)))

print("\nZysk: {0} zł ".format(abs(round(wynik.fun))))
print("Lakierki: {0} sztuk \nSportowe: {1} sztuk".format(abs(round(wynik.x[0])),abs(round(wynik.x[1]))))


'''
l - lakierki
s - Sportowe

2l + s <= 9000   - limit zuzycia skory 1
l + s <= 5500   - limit zuzycia skory 2
l + 2.5s <= 10000  - limit zuzycia skory 3
l >= 100    -min. ilość lakierków
s >= 100    -min. ilość sportowych

150l + 130s -zysk
140l + 250s -koszt
(zysk/ koszt) -> min
'''


