#Anna Wójcik
from scipy.optimize import linprog

SS_lewa = 32+(-6.8/0.55)
SS_prawa = 32+(4.4/0.35)
S_lewa = 24+(-2.8/0.45)
S_prawa = 24+(4.4/0.15)
O_lewa = 48+(-4.4/0.4)
O_prawa = 48+(2.8/0.2)

print("\nWrażliwość rozwiązania optymalnego na zmiany cen akumulatorów")
print("SS: ({0} , {1}) ".format(round(SS_lewa,2),round(SS_prawa,2)))
print("S: ({0} , {1}) ".format(round(S_lewa,2),round(S_prawa,2)))
print("O: ({0} , {1}) ".format(round(O_lewa,2),round(O_prawa,2)))

#--------------------------------------------------------------

A = [[2, 2, 5],[1, 3, 2],[3, 1, 3]]
b = [40, 30, 30]

f = [-32, -24, -48]

wynik= linprog(f, A, b)
print("\n------------------------------------------------------------------")
print("\nPrzed zwiększeniem limitów: ",round((abs(wynik.fun))))

b[0] = b[0] - 10
b[1] = b[1] - 10

wynik2 = linprog(f, A, b)
print("Po zwiększeniu limitów: ",round((abs(wynik2.fun))))
print("W1: {0}\nW2: {1}\nW3: {2}".format(round(wynik2.x[0]),round(wynik2.x[1]),round(wynik2.x[2])))

