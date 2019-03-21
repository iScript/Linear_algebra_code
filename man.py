import numpy as np
import matplotlib.pyplot as plt
import scipy
import sys
from la.Vector import Vector
from la.Matrix import Matrix
from la.LinearSystem import LinearSystem
from la.LinearSystem import inv,rank
from la.LU import lu

# v = Vector([7,-11,1])
# m = Matrix([[1,2,4],[3,7,2],[2,3,3]])
# m2 = Matrix([[0,4,5],[0,0,3]])

# l = LinearSystem(m,v)
# l.gauss_jordan_alimination()
# print(l.fancy_print())


# v = Vector([1,5,13,-1])
# m = Matrix([[1,-1,2,0,3],[-1,1,0,2,-5],[1,-1,4,2,4],[-2,2,-5,-1,-3]])
# l = LinearSystem(m,v)
# l.gauss_jordan_alimination()
# print(l.fancy_print())

# points = [[0,0],[0,5],[3,5],[3,4],[1,4],
# [1,3],[2,3],[2,2],[1,2],[1,0]]  #一个F的点坐标
# x = [point[0] for point in points]
# y = [point[1] for point in points]
# plt.figure(figsize=(5,5))
# plt.xlim(-10,10)
# plt.ylim(-10,10)
# plt.plot(x,y)
# # plt.show()


# P = Matrix(points)
# T = Matrix([[1,2,3],[0,-3,-6],[3,-3,5]])
# T2 = Matrix([[1,0,0],[4,1,0],[0,0,1]])
# P2 = T.dot(T2)
# plt.plot([P2.col_vector(i)[0] for i in range(P2.col_num())],
# [P2.col_vector(i)[1] for i in range(P2.col_num())])
# plt.show()

# print(P2)

# A = Matrix([[1,2,3],[4,5,6],[3,-3,5]])
# L , U = lu(A)
# print(L,U)




A = Matrix([[2,2],[2,1],[1,2]])
print(rank(A))

# print(invA)