# 矩阵类
from .Vector import Vector

# 矩阵类
class Matrix:

    def __init__(self,list2v):
        self._values = [row[:] for row in list2v ]   # 二维数组

    # 零矩阵 r行c列
    @classmethod
    def zero(cls,r,c):
        return cls([[0]*c for _ in range(r)])

    # 单位矩阵，一定是个方阵 , 一个矩阵乘以一个单位矩阵，依然是原矩阵
    @classmethod
    def identity(cls,n):
        m = [[0] * n for _ in range(n)]
        for i in range(n):
            m[i][i] = 1
        return cls(m)

    # 矩阵的转置, 行变成列，列变成行
    def T(self):
        return Matrix([[e for e in self.col_vector(i)]
            for i in range(self.col_num())
        ])

    # 点乘操作
    def dot(self,another):
        #矩阵和向量相乘 ， 矩阵的每一行的向量和向量进行点乘，结果是一个向量
        if isinstance(another,Vector):
            assert self.col_num() == len(another) , "矩阵的列数需和向量的个数一致"
            return Vector([self.row_vector(i).dot(another) for i in range(self.col_num())])
        #矩阵和矩阵相乘, 新的矩阵第i行第j列的元素等于矩阵A的第i行的元素与矩阵B的第j列对应元素乘积之和。
        if isinstance(another,Matrix):
            assert self.col_num() == another.row_num() , "矩阵A的列数需等于矩阵B的行数" 
            return Matrix([ [self.row_vector(i).dot(another.col_vector(j)) for j in range(another.col_num())] for i in range(self.row_num()) ] )


    # 矩阵加法 ， 每个元素相加
    def __add__(self,another):
        assert self.shape() == another.shape() , "shape must same"
        return Matrix([[a+b for a,b in zip(self.row_vector(i),another.row_vector(i))] for i in range(self.row_num()) ])
    # 矩阵减法
    def __sub__(self,another):
        assert self.shape() == another.shape() , "shape must same"
        return Matrix([[a-b for a,b in zip(self.row_vector(i),another.row_vector(i))] for i in range(self.row_num()) ])

    # 矩阵乘法，数量乘
    def __mul__(self,k):
        return Matrix([[e * k for e in self.row_vector(i)] for i in range(self.row_num()) ])

    # 矩阵右乘法
    def __rmul__(self,k):
        return self * k 
    
    # 矩阵除法
    def __truediv__(self,k):
        return (1/k) * self 

    def __pos__(self):
        return 1 * self
    
    def __neg__(self):
        return -1 * self 


    # 返回矩阵第几行
    def row_vector(self,index):
        return Vector(self._values[index])

    # 返回矩阵第几列
    def col_vector(self,index):
        return Vector([row[index] for row in self._values])

    # 
    def __getitem__(self,pos):
        r,c = pos 
        return self._values[r][c]

    def size(self):
        r,c = self.shape()
        return r*c

    def row_num(self):
        return self.shape()[0]

    __len__ = row_num

    def col_num(self):
        return self.shape()[1]

    def shape(self):
        return len(self._values),len(self._values[0])

    # 
    def __repr__(self):
        #format //
        return "__repr__ Matrix({})".format(self._values)

    # 
    __str__ = __repr__