#Anna Wójcik
import cvxopt

M1 = cvxopt.matrix([[10.0, 2.0],
                    [2.0, 1.0]])

M2 = cvxopt.matrix([-10.0, -25.0])

M3 = cvxopt.matrix([[1.0, -1.0, -1.0, 0.0],
                    [2.0, -1.0, 0.0, -1.0]])

M4 = cvxopt.matrix([10.0, -9.0, 0.0, 0.0])

wynik = cvxopt.solvers.qp(M1, M2, M3, M4)

print(wynik['x'])