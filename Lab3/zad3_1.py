# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

def norm(matrix):
    wekt = np.real(matrix)
    suma = sum(wekt)
    return wekt / suma

def prod_wect(matrix):
    rows = len(matrix)
    return_vector = [np.prod(x)** (1/rows) for x in matrix]
    return return_vector

# ZAD1
C_1=[[1,1/7,1/5] , [7,1,3] , [5,1/3,1]]
C_2=[[1,5,9] , [1/5,1,4] , [1/9,1/4,1]] 
C_3=[[1,4,1/5] , [1/4,1,1/9] , [5,9,1]]
C_4=[[1,9,4] , [1/9,1,1/4] , [1/4,4,1]] 
C_5=[[1,1,1] , [1,1,1] , [1,1,1]] 
C_6=[[1,6,4] , [1/6,1,1/3] , [1/4,3,1]]
C_7=[[1,9,6] , [1/9,1,1/3] , [1/6,3,1]] 
C_8=[[1,1/2,1/2] , [2,1,1] , [2,1,1]]

C_parametry=[[1,4,7,5,8,6,6,2] , [1/4,1,5,3,7,6,6,1/3] , [1/7,1/5,1,1/3,5,3,3,1/5] , [1/5,1/3,3,1,6,3,4,1/2] , [1/8,1/7,1/5,1/6,1,1/3,1/4,1/7] , [1/6,1/6,1/3,1/3,3,1,1/2,1/5] , [1/6,1/6,1/3,1/4,4,2,1,1/5] , [1/2,3,5,2,7,5,5,1]]



C_1_norm = norm(prod_wect(C_1))
C_2_norm = norm(prod_wect(C_2))
C_3_norm = norm(prod_wect(C_3))
C_4_norm = norm(prod_wect(C_4))
C_5_norm = norm(prod_wect(C_5))
C_6_norm = norm(prod_wect(C_6))
C_7_norm = norm(prod_wect(C_7))
C_8_norm = norm(prod_wect(C_8))
C_parametry_norm = norm(prod_wect(C_parametry))

macierz = [C_1_norm,C_2_norm,C_3_norm,C_4_norm,C_5_norm,C_6_norm,C_7_norm,C_8_norm]
C = np.transpose(macierz)
ranking = np.matmul(C,C_parametry_norm)
print(ranking)
