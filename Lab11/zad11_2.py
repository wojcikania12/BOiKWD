#Anna Wójcik
import cvxopt


M1 = cvxopt.matrix([[11.4312, 1.1701, 0.1232, 1.6619, 2.0254],
            [1.1701, 7.7723, 0.4983, 1.1374, 1.7056],
            [0.1232, 0.4983, 5.1598, -1.3094, -0.6307],
            [1.6619, 1.1374, -1.3094, 20.2858, 2.2824],
            [2.0254, 1.7056, -0.6307, 2.2824, 4.3189]])

M2 = cvxopt.matrix([0.0, 0.0, 0.0, 0.0, 0.0])

M3 = cvxopt.matrix([-0.94, -1.20, 0.02, -0.81, -0.45]).T

M4 = cvxopt.matrix([-1.0])

M5 = cvxopt.matrix([1.0, 1.0, 1.0, 1.0, 1.0]).T

M6 = cvxopt.matrix([1.0])

wynik = cvxopt.solvers.qp(M1, M2, M3, M4, M5, M6)

print(wynik['x'])
