#Anna Wójcik
import numpy as np
import math

A =np.matrix([[1, 2/3, 2, 5/2, 5/3, 5],
    [3/2,1,3,10/3,3,9],
    [1/2,1/3,1,4/3,7/8,5/2],
    [2/5,3/10,3/4,1,5/6,12/5],
    [3/5,1/3,8/7,6/5,1,3],
    [1/5,1/9,2/5,5/12,1/3,1]])

B= np.matrix([[1, 2/5,3,7/3,1/2,1],
    [5/2,1,4/7,5/8,1/3,3],
    [1/3,7/4,1,1/2,2,1/2],
    [3/7,8/5,2,1,4,2],
    [2,3,1/2,1/4,1,1/2],
    [1,1/3,2,1/2,2,1]])

C = np.matrix([[1,17/4,17/20,8/5,23/6,8/3],
    [4/17,1,1/5,2/5,9/10,2/3],
    [20/17,5,1,21/10,51/10,10/3],
    [5/8,5/2,10/21,1,5/2,11/6],
    [6/23,10/9,10/51,2/5,1,19/30],
    [3/8,3/2,3/10,6/11,30/19,1]])

C_new = np.matrix([[1,17/20,23/6,8/3,17/4,8/5],
    [20/17,1,51/10,10/3,5,21/10],
    [6/23,10/51,1,19/30,10/9,2/5],
    [3/8,3/10,30/19,1,3/2,6/11],
    [4/17,1/5,9/10,2/3,1,2/5],
    [5 / 8, 10 / 21, 5 / 2, 11 / 6, 5 / 2, 1]])

RA = np.array([[3],[1]]) #znany ranking przedmiotu 5,6
RB = np.array([[2], [1/2], [1]]) #znany ranking przedmiotu 4,5,6
RC = np.array([[2], [5]]) #znany ranking przedmiotu 2,4

def koczkodaj(matrix):
    temp = []
    size = len(matrix)
    for i in range(0,size):
        for j in range(0,size):
            for k in range(0,size):
                eq1 = abs(1 - matrix[i, k] * matrix[k, j] / matrix[i, j])
                eq2= abs(1 - matrix[i, j] / (matrix[i, k] * matrix[k, j]))
                minimum = min(eq1, eq2)
                temp.append(minimum)
    result = max(temp)
    return result


def rank_aryt(len,unknown_obj_matrix,known_obj_matrix,k,known_obj_rank,last = True):
    for i in range(len - k):
        for j in range(len - k):
            if (i != j):
                unknown_obj_matrix[i, j] = unknown_obj_matrix[i, j] * (-1 / (len - 1))
    b = ((1 / (len - 1)) * known_obj_matrix * known_obj_rank)
    W = np.linalg.inv(unknown_obj_matrix) * b # AW = b -> W = A^-1B
    if(last):
        result = np.concatenate((W, known_obj_rank))
    else:
        result = np.array([W[0],known_obj_rank[0].tolist(),W[1],known_obj_rank[1],W[2],W[3]])
    return result



# HRE z wartością średnią arytmetyczną

equation = lambda matrix_,k : 1 - ((1+math.sqrt(4*(len(matrix_)-1)*(len(matrix_)-k-2))) / (2*(len(matrix_)-1)))

names = ["A", "B", "C"]
matrix = [A, B, C_new]
k = [2,3,2]
for i in range(0,3):
    temp  = matrix[i]
    if koczkodaj(temp) < equation(temp, k[i]):
        print("Macierz "+ names[i] + " - pewny wynik")
    else:
        print("Macierz "+ names[i] + " - niepewny wynik")

unknown_obj_A =np.matrix([[1, 2/3, 2, 5/2],
                [3/2,1,3,10/3],
                [1/2,1/3,1,4/3],
                [2/5,3/10,3/4,1]])
known_obj_A = np.matrix([[ 5/3, 5],
                [3,9],
                [7/8,5/2],
                [5/6,12/5]])
unknown_obj_B = np.matrix([[1, 2/5,3],
                [5/2,1,4/7],
                [1/3,7/4,1]])
known_obj_B = np.matrix([[7/3,1/2,1],
                [5/8,1/3,3],
                [1/2,2,1/2]])


unknown_obj_C = np.matrix([[1,17/20,23/6,8/3],
    [20/17,1,51/10,10/3],
    [6/23,10/51,1,19/30],
    [3/8,3/10,30/19,1]])

known_obj_C = np.matrix([[17/4,8/5],
    [5,21/10],
    [10/9,2/5],
    [3/2,6/11]])


rankingA = rank_aryt(len(A), unknown_obj_A, known_obj_A, 2, RA)
rankingB = rank_aryt(len(B), unknown_obj_B, known_obj_B, 3, RB,)
rankingC = rank_aryt(len(C_new), unknown_obj_C, known_obj_C, 2, RC,False)


print(" ")
ranking =[rankingA,rankingB,rankingC]
for i in range(0,3):
    temp  = ranking[i]
    print("Ranking macierzy "+ names[i] + " m. arytm. : ")
    print(ranking[i] )
    print(" ")








