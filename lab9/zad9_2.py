#Anna Wójcik

from scipy.optimize import linprog

A = [[8, 6, 1], [8, 4, 3], [4, 3, 1]]
b = [960, 800, 320]

f = [-60, -30, -20]

wynik = linprog(f,A, b)

print("\nPrzed zwiększeniem: ",round((abs(wynik.fun))))

#--------------------------------------------------------------

f[1] = -40
wynik2 = linprog(f,A, b)
print("Po zwiększeniu: ",round((abs(wynik2.fun))))
print("Zwiększenie ceny stołów do 40 zl zmienia wynik.")

#--------------------------------------------------------------
lawki_lewa = 60 + (-5/1.25)
lawki_prawa = 60 + (5/0.25)
krzesla_lewa = 20 +(-5)
krzesla_prawa = 20 + (5/2)

print("\n------------------------------------------------------------------")
print("\nPrzedziały nie powodujące zmian:")
print("Ławki: ({0} , {1}) ".format(lawki_lewa,lawki_prawa))
print("Krzesła: ({0} , {1}) ".format(krzesla_lewa,krzesla_prawa))

#--------------------------------------------------------------
print("\n------------------------------------------------------------------")

f[1] = -30
b[2] = 400
wynik3 = linprog(f,A, b)
print("\nRozwiązanie optymalne w przypadku, gdy dopuszczalny czas pracy wykańczalni wzrośnie do 400 godzin:",round((abs(wynik3.fun))))
