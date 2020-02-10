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

def rank_geo(matrix,k,known_obj_rank,last = True):
    n = len(matrix)
    vn = len(known_obj_rank)
    A = np.full((n - k , n - k), -1)
    np.fill_diagonal(A, n-1)
    b = []
    for i in range(0,n - k):
        val = 1
        for j in range(0,vn):
            val = val * known_obj_rank[j]
        for k in range(0,n):
            val = val * matrix[i,k]
        log_val = math.log10(val)
        b.append(log_val)

    W = np.linalg.solve(A, b)
    W2 = [[10 ** W[i]] for i in range(len(W))]

    if(last):
        result = np.concatenate((W2, known_obj_rank))
    else:
        result = np.array([W2[0],known_obj_rank[0].tolist(),W2[1],known_obj_rank[1].tolist(),W2[2],W2[3]])
    return result

rankingA_geo = rank_geo(A,2,RA)
rankingB_geo = rank_geo(B,3,RB)
rankingC_geo = rank_geo(C_new,2,RC,False)

names = ["A", "B", "C"]
matrix = [A, B, C_new]
print(" ")
ranking =[rankingA_geo,rankingB_geo,rankingC_geo]
for i in range(0,3):
    temp  = ranking[i]
    print("Ranking macierzy "+ names[i] + " m. geom. : ")
    print(ranking[i] )
    print(" ")

