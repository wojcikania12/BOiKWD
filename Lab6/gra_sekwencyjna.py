#Anna Wojcik
import math
from copy import deepcopy


def wypisz_wynik(wynik):
    if (wynik > 0):
        print('Wygrywa gracz 1')
    elif (wynik == 0):
        print('Remis')
    else:
        print('Wygrywa gracz 2')
    print("Różnica pkt : ", abs(wynik))
    print(' ')


def falsz_macierz():
    return [[False for x in range(3)] for i in range (2)]

def inicjalizacja_wyniku_gracza(gracz):
    wynik = 0
    if gracz == 0 :
        wynik = -math.inf
    else:
        wynik = math.inf
    return wynik


class Wezel:
    def __init__(self):
        self.potomkowie = []
        self.wynik = 0


def wynik_etapu_gry(wezel,zabraneMonety,odwiedzone,stanStosu,obecnyGracz):
    wezel.wynik = zabraneMonety[0] - zabraneMonety[1]
    for i in range(len(stanStosu)):
        if not odwiedzone[obecnyGracz][i]:
            wezel.wynik = wezel.wynik + stanStosu[i]
        if not odwiedzone[1 - obecnyGracz][i]:
            wezel.wynik = wezel.wynik - stanStosu[i]



def ruch(wezel, stanStosu, odwiedzone, zabraneMonety, obecnyGracz, obecnyRuch):
    wezel.wynik = inicjalizacja_wyniku_gracza(obecnyGracz)
    wezel_koncowy = True

    for i in range(len(stanStosu)):
        if (not odwiedzone[obecnyGracz][i]):
            for j in range(1, min(max(1, obecnyRuch), stanStosu[i]) + 1):

                wezel_koncowy = False

                res = zabraneMonety.copy()
                res[obecnyGracz] =  res[obecnyGracz] + j
                nowyStatusStosu= stanStosu.copy()
                nowyStatusStosu[i] = nowyStatusStosu[i] - j
                kolejnyRuch= deepcopy(odwiedzone)
                kolejnyRuch[obecnyGracz][i] = True
                nowy = Wezel()
                wezel.potomkowie.append(nowy)

                max_ilosc = j * 2
                ruch(nowy, nowyStatusStosu, kolejnyRuch, res, 1 - obecnyGracz, max_ilosc)

                if obecnyGracz != 0:
                    wezel.wynik = min(wezel.wynik, nowy.wynik)
                else:
                    wezel.wynik = max(wezel.wynik, nowy.wynik)

    if wezel_koncowy:
        wynik_etapu_gry(wezel,zabraneMonety,odwiedzone,stanStosu,obecnyGracz)

    return wezel


stos1 = [2, 2, 2]
stos2 = [3, 3, 3]
stos3 = [1, 2, 6]
wypisz_wynik(ruch(Wezel(), stos1, falsz_macierz(), [0, 0], 0, 1).wynik)
wypisz_wynik(ruch(Wezel(), stos2, falsz_macierz(), [0, 0], 0, 1).wynik)
wypisz_wynik(ruch(Wezel(), stos3, falsz_macierz(), [0, 0], 0, 1).wynik)
