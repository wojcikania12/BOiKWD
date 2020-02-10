import numpy as np

def normalizacja(matrix, col):
    wekt = np.real(matrix[:, col])
    suma = sum(wekt)
    return wekt / suma

#-----------------Podkryteria pojemnosc: rozmiar, pasaz--------------------

rozmiar= [[1, 6, 3],
          [1/6, 1, 1/2],
          [1/3, 2, 1]]

pasazerowie= [[1, 1, 3],
              [1, 1, 3],
              [1/3, 1/3, 1]]
Cp1 = [[1,6],  #pasazerowie wazniejsi
       [1/6,1]]

[Cp1_wart, Cp1_wekt]  = np.linalg.eig(Cp1)
[rozmiar_wart, rozmiar_wekt]  = np.linalg.eig(rozmiar)
[pasazerowie_wart, pasazerowie_wekt]  = np.linalg.eig(pasazerowie)

Cp1_norm = normalizacja(Cp1_wekt, 0)
rozmiar_norm = normalizacja(rozmiar_wekt, 0)
pasazerowie_norm = normalizacja(pasazerowie_wekt, 1)

C = np.transpose([pasazerowie_norm, rozmiar_norm, ])
pojemnosc_ranking= np.matmul(C,Cp1_norm)


#----------------------Podkryteria ceny: cena_sam, cena_paliwa---------------

cena_sam = [[1, 1/6, 2],
            [6, 1, 7],
            [1/2, 1/7, 1]]
cena_paliwa = [[1, 6, 1/3],
               [1/6, 1, 1/8],
               [3, 8, 1]]
Cp2 = [[1, 7],  #cena sam. ważniejsza
       [1/7, 1]]

[Cp2_wart, Cp2_wekt]  = np.linalg.eig(Cp2)
[cena_sam_wart, cena_sam_wekt]  = np.linalg.eig(cena_sam)
[cena_paliwa_wart, cena_paliwa_wekt]  = np.linalg.eig(cena_paliwa)

Cp2_norm = normalizacja(Cp2_wekt, 0)
cena_sam_norm = normalizacja(cena_sam_wekt, 0)
cena_paliwa_norm = normalizacja(cena_paliwa_wekt, 0)

C2 = np.transpose([cena_sam_norm,cena_paliwa_norm])
cena_ranking= np.matmul(C2,Cp2_norm)


#-----------------kryteria------------------
cena = [[1, 1/8, 3],
        [8, 1, 9],
        [1/3, 1/9, 1]]

bezpieczenstwo = [[1, 4, 1/6],
                  [1/4, 1, 1/8],
                  [6, 8, 1]]

pojemnosc = [[1, 2, 4],
             [1/2, 1, 3],
             [1/4, 1/3, 1]]

Cp3 = [[1, 2 , 4],  #najwazniejsza cena, potem bezpiecz.
       [1/2, 1, 3],
       [1/4, 1/3, 1]]

[Cp3_wart, Cp3_wekt]  = np.linalg.eig(Cp3)
[cena_wart, cena_wekt]  = np.linalg.eig(cena)
[bezpieczenstwo_wart, bezpieczenstwo_wekt]  = np.linalg.eig(bezpieczenstwo)
[pojemnosc_wart, pojemnosc_wekt]  = np.linalg.eig(pojemnosc)


Cp3_norm = normalizacja(Cp3_wekt, 0)
cena_norm = normalizacja(cena_wekt, 0)
bezpieczenstwo_norm = normalizacja(bezpieczenstwo_wekt, 0)
pojemnosc_norm = normalizacja(pojemnosc_wekt, 0)

C3 = np.transpose([cena_norm,bezpieczenstwo_norm,pojemnosc_norm])
ranking= np.matmul(C3,Cp3_norm)

print(ranking)




