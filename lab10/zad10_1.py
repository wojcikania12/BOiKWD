#Anna Wójcik

from scipy.optimize import linprog

A = [[1,1], [1,2],[-2,-1]]
b = [350, 500, -600]
f = [3, 2]
wynik = linprog(f,A, b,bounds =((0, None),(0 ,None)))

print("Produkt A: {0} sztuk \nProdukt B: {1} sztuk".format(abs(round(wynik.x[0])),abs(round(wynik.x[1]))))


'''
a - Produkt A
b - Produkt B

a + b <= 350    - limit surowca
a + 2b <= 500   - limit czasu
2a + b >= 600   - minimalny zysk ze sprzedaży

3a + 2b -> max   - produktywność (wartość produktu w cenie zbytu /zużyty czas)
'''





