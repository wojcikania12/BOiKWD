#Anna Wójcik
A= [[1,2/3,2,5/2,5/3,5],[3/2,1,3,10/3,3,9],[1/2,1/3,1,4/3,7/8,5/2],[2/5,3/10,3/4,1,5/6,12/5],[3/5,1/3,8/7,6/5,1,3],[1/5,1/9,2/5,5/12,1/3,1]]

B= [[1,2/5,3,7/3,1/2,1,2],[5/2,1,4/7,1,1,3,2/3],[1/3,7/4,1,1/2,2,1/2,1],[3/7,1,2,1,4,2,6],[2,1,1/2,1/4,1,1/2,3/4],[1,1/3,2,1/2,2,1,5/8],[1/2,3/2,1,1/6,4/3,8/5,1]]

C= [[1,2/3,2/15,1,8,12/5,1,1/2],[3/2,1,1,2,1,2/3,1/6,1],[15/2,1,1,5/2,7/8,2,1,1/5],[1,1/2,2/5,1,4/3,1,2/7,1],[1/8,1,8/7,3/4,1,1/5,2/7,1],[5/12,3/2,1/2,1,5,1,3,2],[1,6,1,7/2,7/2,1/3,1,3/11],[2,1,5,1,1,1/2,11/3,1]]

D= [[0,1,1,-1,-1,1,-1],[-1,0,0,1,1,-1,0],[-1,0,0,0,1,1,-1],[1,-1,0,0,1,0,1],[1,0,-1,-1,0,1,-1],[-1,1,-1,1,-1,0,0],[1,0,1,-1,1,0,0]]

E= [[0,1,0,0,-1],[-1,0,0,0,1],[0,0,0,1,0],[0,0,-1,0,0],[1,-1,0,0,0]]

F= [[0,-1,1,-1,1,-1,1,-1,1],[1,0,1,1,1,-1,-1,-1,-1],[-1,-1,0,-1,1,-1,1,1,1],[1,-1,1,0,-1,1,-1,1,-1],[-1,-1,-1,1,0,-1,1,1,1],[1,1,1,-1,1,0,-1,-1,-1],[-1,1,-1,1,-1,1,0,1,-1],[1,1,-1,-1,-1,1,-1,0,1],[-1,1,-1,1,-1,1,1,-1,0]]

def generalized_tourney(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = matrix.copy()
    for i in range(rows):
        for j in range(cols):
            if (result[i][j]) > 1:
                result[i][j] = 1
            elif (result[i][j] == 1):
                result[i][j] = 0
            else:
                result[i][j] = -1
    return result

def is_generalized_tourney(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    x = 0
    result = ""
    for i in range(rows):
        for j in range(cols):
            if (i != j and matrix[i][j] != -matrix[j][i]):
                result = "Macierz nieturniejowa. "
                return result
            if(i != j and matrix[i][j] == 0):
                x = x + 1
    if(result == ""):
        result = "Macierz turniejowa. "
    if(x):
        result = result + " Uogólniona. Są remisy"
    else:
        result = result + " Nieuogólniona."
    return result


def generalized_Kendall(matrix):
    three = 0
    size = len(matrix)
    for i in range(0,size):
        for j in range(i,size):
            for k in range(j,size):
                if(i != j != k):
                    #trójka z jedną krawędzią skierowaną
                    if(matrix[i][j] == 0 and  matrix[j][k] ==0 and  matrix[k][i] !=0 ):
                        three = three + 1
                    if(matrix[i][j] == 0 and  matrix[j][k] != 0 and  matrix[k][i] ==0 ):
                        three = three + 1
                    if(matrix[i][j] != 0 and  matrix[j][k] ==0 and  matrix[k][i] ==0 ):
                        three = three + 1
                    #trójka z dwiema krawędziami skierowanymi
                    if (matrix[i][j] == matrix[j][k] != 0 and  matrix[k][i] ==0 ):
                        three = three + 1
                    if (matrix[i][j] == 0 and matrix[j][k] ==  matrix[k][i] !=0 ):
                        three = three + 1
                    if (matrix[i][j] == matrix[k][i] !=0  and  matrix[j][k] == 0):
                        three = three + 1
                    #trójka z trzema krawędziami skierowanymi
                    if(matrix[i][j] == matrix[j][k] == matrix[k][i] != 0):
                        three = three + 1
    if(size % 4 == 0):
        result = (13*size**3-24*size**2-16*size)/96
    elif(size % 4 == 1):
        result = (13*size**3-24*size**2-19*size +30)/96
    elif(size % 4 == 2):
        result = (13*size**3-24*size**2-4*size)/96
    else:
        result = (13*size**3-24*size**2-19*size+18)/96
    return 1 - three/result


def classic_Kendall(matrix):
    three = 0
    size = len(matrix)
    for i in range(0,size):
        for j in range(i,size):
            for k in range(j,size):
                if(i != j != k):
                    if(matrix[i][j] == matrix[j][k] == matrix[k][i]):
                        three =  three + 1
    if(size % 2 != 0):
        result = (size**3-size)/24
    else:
        result = (size**3-4*size)/24

    return 1 - three/result

#przekształcamy na turniejowe
A = generalized_tourney(A)
B = generalized_tourney(B)
C = generalized_tourney(C)

print("A: ", is_generalized_tourney(A))
print("B: ", is_generalized_tourney(B))
print("C: ", is_generalized_tourney(C))
print("D: ", is_generalized_tourney(D))
print("E: ", is_generalized_tourney(E))
print("F: ", is_generalized_tourney(F))

print("\nKlasyczny indeks Kendalla dla macierzy turniejowych nieuogólnionych:")
print("A:", classic_Kendall(A))
print("F:", classic_Kendall(F))


print("\nUogólniony indeks Kendalla dla macierzy turniejowych:")
print("A:", generalized_Kendall(A))
print("B:", generalized_Kendall(B))
print("C:", generalized_Kendall(C))
print("E:", generalized_Kendall(E))
print("F:", generalized_Kendall(F))

