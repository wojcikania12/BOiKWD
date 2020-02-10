import numpy as np

def normalizacja(matrix, col):
    wekt = np.real(matrix[:, col])
    suma = sum(wekt)
    return wekt / suma


C1 = [[1, 1/7, 1/5],
      [7, 1, 3],
      [5, 1/3, 1]]

C2 = [[1, 5, 9],
      [1/5, 1, 4],
      [1/9, 1/4, 1]]

C3 = [[1, 4, 1/5],
      [1/4, 1, 1/9],
      [5, 9, 1]]

C4 = [[1, 9, 4],
      [1/9, 1, 1/4],
      [1/4, 4,1]]

C5 = [[1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]]

C6 = [[1, 6, 4],
      [1/6, 1, 1/3],
      [1/4, 3, 1]]

C7 = [[1, 9, 6],
      [1/9, 1, 1/3],
      [1/6, 3, 1]]

C8 = [[1, 1/2, 1/2],
      [2, 1, 1],
      [2, 1, 1]]

Cp = [[1, 4, 7, 5, 8, 6, 6, 2],
     [1 / 4, 1, 5, 3, 7, 6, 6, 1 / 3],
     [1 / 7, 1 / 5, 1, 1 / 3, 5, 3, 3, 1 / 5],
     [1 / 5, 1 / 3, 3, 1, 6, 3, 4, 1 / 2],
     [1 / 8, 1 / 7, 1 / 5, 1 / 6, 1, 1 / 3, 1 / 4, 1 / 7],
     [1 / 6, 1 / 6, 1 / 3, 1 / 3, 3, 1, 1 / 2, 1 / 5],
     [1 / 6, 1 / 6, 1 / 3, 1 / 4, 4, 2, 1, 1 / 5],
    [1 / 2, 3, 5, 2, 7, 5, 5, 1]]


[C1_wart, C1_wekt] = np.linalg.eig(C1)
[C2_wart, C2_wekt] = np.linalg.eig(C2)
[C3_wart, C3_wekt] = np.linalg.eig(C3)
[C4_wart, C4_wekt] = np.linalg.eig(C4)
[C5_wart, C5_wekt] = np.linalg.eig(C5)
[C6_wart, C6_wekt] = np.linalg.eig(C6)
[C7_wart, C7_wekt] = np.linalg.eig(C7)
[C8_wart, C8_wekt] = np.linalg.eig(C8)
[Cp_wart, Cp_wekt] = np.linalg.eig(Cp)

C1_norm = normalizacja(C1_wekt, 0)
C2_norm = normalizacja(C2_wekt, 0)
C3_norm = normalizacja(C3_wekt, 0)
C4_norm = normalizacja(C4_wekt, 0)
C5_norm = normalizacja(C5_wekt, 1)
C6_norm = normalizacja(C6_wekt, 0)
C7_norm = normalizacja(C7_wekt, 0)
C8_norm = normalizacja(C8_wekt, 1)
Cp_norm = normalizacja(Cp_wekt, 0)

macierz = [C1_norm,C2_norm,C3_norm,C4_norm,C5_norm,C6_norm,C7_norm,C8_norm]
C = np.transpose(macierz)
ranking = np.matmul(C,Cp_norm)
print(ranking)
