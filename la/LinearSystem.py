
from .Matrix import Matrix
from .Vector import Vector
from ._global import is_zero

class LinearSystem:

    def __init__(self,A,b=None):
        
        assert b is None or A.row_num() == len(b) , "矩阵行数需等于向量个数 或者 b是None"
        
        # m n 行数 列数 
        self._m = A.row_num()
        self._n = A.col_num()
        
        # assert self._m == self._n , "临时限制"

        if b is None :
            self.Ab = [A.row_vector(i) for i in range(self._m)]

        if isinstance(b,Vector):
            # 将向量的第i个元素，放到矩阵第i行的后面
            self.Ab = [Vector(A.row_vector(i).underlying_list() + [b[i]]) 
                    for i in range(self._m) ]
        if isinstance(b,Matrix):
            self.Ab = [Vector(A.row_vector(i).underlying_list() + b.row_vector(i).underlying_list()) 
                    for i in range(self._m) ]


        # 存储主元位置，key=行 value=该行主元位置
        self.pivots = []


    # 参数 index_i行 index_j列 n行的最大值 
    # 循环i行到最大行，哪一行index_j的值最大，则返回该行数。
    def _max_row(self,index_i,index_j,n):
        best , ret = self.Ab[index_i][index_j] , index_i
        for i in range(index_i+1 ,n):   # range(start,stop) ， 从第index_i行到最后
            if self.Ab[i][index_j] > best:
                best,ret = self.Ab[i][index_j] , i
        return ret

    # 前向过程
    def _forward(self):
        i,k = 0,0

        #遍历每一行  i小于行数 k小于列数
        while i<self._m and k<self._n:
            # k位置最大行
            max_row = self._max_row(i,k,self._m)
            # 最大行和当前行交换位置
            self.Ab[i] , self.Ab[max_row] = self.Ab[max_row] , self.Ab[i] 

            # 
            if is_zero(self.Ab[i][k])  :
                k += 1
            else:
                # 将主元归为一
                self.Ab[i] = self.Ab[i] / self.Ab[i][k] 
                
                #遍历该行下面的那行，k这个位置化为0
                for j in range(i+1,self._m):
                    # 上一行的主元为1，乘以self.Ab[j][i]，即相同，可消
                    # 下面每一行和i行相减，相减之后使第k列减为0
                    self.Ab[j] = self.Ab[j] - self.Ab[j][k] * self.Ab[i]    
                self.pivots.append(k)   # k 这列是主元列 
                i += 1



    def _backward(self):
        n = len(self.pivots)
        # range(start, stop[, step])
        # 从最后一行到第0行遍历
        for i in range(n-1,-1,-1):
            
            k = self.pivots[i]
            # Ab[i][k] 为主元
            #循环i上面的每一行，消
            for j in range(i-1,-1,-1):
                self.Ab[j] = self.Ab[j] - self.Ab[j][k] * self.Ab[i]    


    # 高斯约旦消元法
    def gauss_jordan_alimination(self):
        self._forward() # 前向过程 高斯
        self._backward()# 后向过程 约旦

        # 是否有解
        for i in range(len(self.pivots),self._m):
            #全为0的行 ， 最后一个元素不为0
            if not is_zero(self.Ab[i][-1]):
                return False
        return True

    def fancy_print(self):
        for i in range(self._m):
            print(" ".join( str(self.Ab[i][j]) for j in range(self._n) ) , end = " ")
            print("|",self.Ab[i][-1])


# function 解矩阵的逆
def inv(A):
    # 如果行列不相等，没有逆矩阵
    if A.row_num() != A.col_num() :
        return None
    
    n = A.row_num()

    # 创建线性系统
    ls = LinearSystem(A,Matrix.identity(n))
   


    # 无解，没有逆矩阵
    if not ls.gauss_jordan_alimination():
        return None

    # print(ls.Ab)
    # return

    # 向量放在矩阵后面，消元后，后面就是解 (同理矩阵放矩阵后面，消元后，后面就是解)
    # 后面的矩阵就是多个向量的拼接 ，因为如果分开解的话，前面的矩阵都是相同的，所以可拼接
    # 解就是逆矩阵
    invA = [[row[i] for i in range(n,2*n)] for row in ls.Ab ]
    return Matrix(invA)


# 解矩阵的秩
def rank(A):
    ls = LinearSystem(A)
    ls.gauss_jordan_alimination()   
    print(A.col_num())
    zero = Vector.zero(A.col_num())
    # 所有非零行就是矩阵的秩
    return sum([row != zero for row in ls.Ab])