#Anna Wójcik
import numpy as np

A=[[1,7,3] , [1/7,1,2] , [1/3,1/2,1]]
B=[[1,1/5,7,1] , [5,1,1/2,2] , [1/7,2,1,3] , [1,1/2,1/3,1]]
C=[[1,2,5,1,7] , [1/2,1,3,1/2,5] , [1/5,1/3,1,1/5,2] , [1,2,5,1,7] , [1/7,1/5,1/2,1/7,1]]


def satty(macierz):
    [M_wart, M_wekt] = np.linalg.eig(macierz)
    wart_max = max(M_wart)
    result = (wart_max - len(macierz))/(len(macierz) -1)
    return np.real(result)

def norm(matrix):
    wekt = np.real(matrix)
    suma = sum(wekt)
    return wekt / suma

def prod_wect(matrix):
    rows = len(matrix)
    return_vector = [np.prod(x)** (1/rows) for x in matrix]
    return return_vector


def blad(macierz,macierz2,i,j):
    return (macierz[i][j] * (macierz2[i]/macierz2[j]))
        


def geom(macierz,macierz2):
    wymiar = len(macierz)
    suma = 0
    for i in range(wymiar):
        for j in range(i+1, wymiar):
            e = blad(macierz,macierz2,i,j)
            suma += np.log10(e)**2
    I = (2 / ((wymiar - 1)*(wymiar - 2))) * suma
    return I

def koczkodaj(matrix):
    temp = []
    size = len(matrix)
    for i in range(0,size):
        for j in range(0,size):
            for k in range(0,size):
                eq1 = abs(1 - matrix[i][k] * matrix[k][j] / matrix[i][j])
                eq2= abs(1 - matrix[i][j] / (matrix[i][k] * matrix[k][j]))
                minimum = min(eq1, eq2)
                temp.append(minimum)
    result = max(temp)
    return result


# Satty
    
A_satty = satty(A)
B_satty = satty(B)
C_satty = satty(C)

names = ["A", "B", "C"]
ind =[A_satty, B_satty, C_satty]
for i in range(0,3):
    temp  = ind[i]
    print("Indeksy spójności Satty’ego macierzy " + names[i] + " : " )
    print(ind[i])
print(" ")

# Geometryczna
A_prod = norm(prod_wect(A))
B_prod = norm(prod_wect(B))
C_prod = norm(prod_wect(C))

A_geom = geom(A,A_prod)
B_geom = geom(B,B_prod)
C_geom = geom(C,C_prod)

ind =[A_geom, B_geom, C_geom]
for i in range(0,3):
    temp  = ind[i]
    print("Indeksy geometryczny macierzy "+ names[i] + " : ")
    print(ind[i])
print(" ")


#Koczkodaj

A_koczkodaj = koczkodaj(A)
B_koczkodaj = koczkodaj(B)
C_koczkodaj = koczkodaj(C)

ind =[A_koczkodaj, B_koczkodaj, C_koczkodaj]
for i in range(0,3):
    temp  = ind[i]
    print("Indeks niespójności Koczkodaja macierzy "+ names[i] + " : ")
    print(ind[i])
