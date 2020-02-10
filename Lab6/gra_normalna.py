#Anna Wójcik
import numpy as np

Matrix = np.array([[20, -150, -250], [150, -80, -100], [250, 100, 40]])

A = max(min(Matrix[0]), min(Matrix[1]), min(Matrix[2]))
B = min(max(Matrix[:,0]), max(Matrix[:,1]), max(Matrix[:,2]))

print('A:{0}'.format(A))
print('B:{0}'.format(B))
print('Najkorzystniejsza decyzja dla obu producentów to uruchomienie produkcji 300 tys. sztuk.')