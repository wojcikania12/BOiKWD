import numpy as np

def normalizacja(matrix, col):
    wekt = np.real(matrix[:, col])
    suma = sum(wekt)
    return wekt / suma


cena= [[1,1/7,2,4],
       [7,1,8,9],
       [1/2,1/8,1,2],
       [1/4,1/9,1/2,1]]

wyzywienie= [[1,1,8,4],
             [1,1,8,4],
             [1/8,1/8,1,1/3],
             [1/4,1/4,3,1]]

odleglosc = [[1,3,1/2,1/5],
             [1/3,1,1/5,1/7],
             [2,5,1,1/2],
             [5,7,2,1]]

parking = [[1,1/8,1,1/8],
           [8,1,8,1],
           [1,1/8,1,1/8],
           [8,1,8,1]]

Cp= [[1,5,3,4],
    [1/5,1,4,1],
    [1/3,1/4,1,2],
    [1/4,1,1/2,1]]

[cena_wart, cena_wekt] = np.linalg.eig(cena)
[wyzywienie_wart, wyzywienie_wekt] = np.linalg.eig(wyzywienie)
[odleglosc_wart, odleglosc_wekt] = np.linalg.eig(odleglosc)
[parking_wart, parking_wekt] = np.linalg.eig(parking)
[Cp_wart, Cp_wekt] = np.linalg.eig(Cp)

cena_norm = normalizacja(cena_wekt, 0)
wyzywienie_norm = normalizacja(wyzywienie_wekt, 0)
odleglosc_norm = normalizacja(odleglosc_wekt, 0)
parking_norm = normalizacja(parking_wekt, 1)
Cp_norm = normalizacja(Cp_wekt, 0)


macierz = [cena_norm,wyzywienie_norm,odleglosc_norm,parking_norm]
C = np.transpose(macierz)
ranking = np.matmul(C,Cp_norm)
print(ranking)

