import math
from ._global import EPSILON,is_equal

# 向量类
class Vector:
    def __init__(self,list):
        self._values = list

    # 类方法，不需要实例化 。 实现零向量
    @classmethod
    def zero(cls,dim):
        return cls([0] * dim)

    # 实现向量的模，即长度 , 各个向量平方和开根
    def norm(self):
        return math.sqrt(sum(e**2 for e in self._values))

    # 单位向量，即归一化
    def normalize(self):
        if self.norm() < EPSILON: #浮点数不能直接判断0
            raise ZeroDivisionError("单位向量为0")
        return Vector(self._values) / self.norm()

    # 返回向量的列表副本
    def underlying_list(self):
        return self._values[:]

    # 实现向量加法
    def __add__(self,another):
        # assert断言，为假会触发异常
        assert len(self) == len(another) , "Error in add , length of v must same."
        #print("test")
        return Vector([a+b for a,b in zip(self,another)])



    # 实现向量减法
    def __sub__(self,another):
        assert len(self) == len(another) , "Error in sub , length of v must same."
        return Vector([a-b for a,b in zip(self,another)])

    # 向量点乘
    def dot(self,another):
        assert len(self) == len(another) , "Error in sub , length of v must same."
        return sum(a*b for a,b in zip(self,another))


    # 向量乘法
    def __mul__(self,k):
        return Vector([k*e for e in self])

    # 向量乘法
    def __rmul__(self,k):
        return self * k

    # 向量除法
    def __truediv__(self,k):
        return (1/k) * self
    
    # 取正
    def __pos__(self):
        return 1* self

    # 取负
    def __neg__(self):
        return -1* self

    # 2个向量是否相等
    def __eq__(self,other):
        other_list = other.underlying_list()
        if( len(other_list) != len(self._values) ):
            return False
        return all(is_equal(x,y) for x,y in zip(self._values,other_list))

    def __neq__(self,other):
        return not(self == other)


    def __getitem__(self,index):
        return self._values[index]

    def __len__(self):
        return len(self._values)

    def __iter__(self):
        # 返回向量的迭代器。（原本for循环需要o._value，现在直接o）
        return self._values.__iter__()

    # 
    def __repr__(self):
        #format //
        return "__repr__ Vector({})".format(self._values)

    # 
    def __str__(self):
        # 通过comprehension创建list，然后list元素用,相连
        return "__str__ ({})".format(",".join(str(e) for e in self._values))

# comprehension