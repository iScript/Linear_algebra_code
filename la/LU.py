from .Matrix import Matrix
from .Vector import Vector
#from ._global import iz_zero
from ._global import is_zero


# 

def lu(matrix):
    
    # 暂时只实现方阵的LU分解
    assert matrix.row_num() == matrix.col_num() , "must be a aquare matrix"

    n = matrix.row_num()
    A = [matrix.row_vector(i) for i in range(n)]
    L = [[1.0 if i == j else 0.0 for i in range(n) ] for j in range(n)]

    for i in range(n):
        # 看A[i][i]是否可以是主元
        if is_zero(A[i][i]):
            return None,None
        else:
            for j in range(i+1,n):
                p = A[j][i] / A[i][i]
                A[j] = A[j]  - p * A[i]
                L[j][i] = p

    return Matrix(L) , Matrix([A[i].underlying_list() for i in range(n)])