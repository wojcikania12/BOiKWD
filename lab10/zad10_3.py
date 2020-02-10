#Anna Wójcik

from scipy.optimize import linprog

A = [[4,3], [1,1]]
b = [190, 55]
f = [-23, -17]
wynik = linprog(f,A, b,bounds =((0, None),(0 ,None)))
print("1. ",wynik.x)

A = [[4,3], [1,1],[1,0]]
b = [190, 55, 47]
wynik = linprog(f,A, b,bounds =((0, None),(0 ,None)))
print("2. ",wynik.x)

A = [[4,3], [1,1],[1,0], [0 ,-1]]
b = [190, 55, 47, -1]
wynik = linprog(f,A, b,bounds =((0, None),(0 ,None)))
print("3. ",wynik.x)

A = [[4,3], [1,1],[1,0], [0 ,-1]]
b = [190, 55, 46, -1]
wynik = linprog(f,A, b,bounds =((0, None),(0 ,None)))
print("4. ",wynik.x)


print("\n-----WYNIK------\nŁańcuszki: {0} sztuk \nPierścionki: {1} sztuk".format(abs(round(wynik.x[0])),abs(round(wynik.x[1]))))

'''
l - lancuszki
p - pierscionki

4l + 3p <= 190   - limit zuzycia złota
l + p <= 55   - limit zuzycia masy perłowej

23l + 17p -> max  -zysk
'''


