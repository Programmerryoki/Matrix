from typing import List


class Matrix2D:
    matrix = None

    def __init__(self, size: (int, int) = None,
                 matrixlist: List[List[int]] = None,
                 matrix: "Matrix2D" = None):
        if size:
            self.matrix = [[0]*size[1] for _ in range(size[0])]
        elif matrixlist:
            size = (len(matrixlist), len(matrixlist[0]))
            self.matrix = [[0]*size[1] for _ in range(size[0])]
            try:
                for i in range(size[0]):
                    for j in range(size[1]):
                        self.matrix[i][j] = matrixlist[i][j]
            except IndexError:
                self.matrix = None
        elif matrix:
            size = matrix.size()
            self.matrix = [[0]*size[1] for _ in range(size[0])]
            for i in range(size[0]):
                for j in range(size[1]):
                    self.matrix[i][j] = matrix.matrix[i][j]

    def size(self) -> (int, int):
        return len(self.matrix), len(self.matrix[0])

    def __eq__(self, other: "Matrix2D") -> bool:
        if self.size() != other.size():
            return False
        size = self.size()
        for i in range(size[0]):
            for j in range(size[1]):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True
    
    def __bool__(self) -> bool:
        return bool(self.size() and self.matrix)

    def __add__(self, other: "Matrix2D") -> "Matrix2D":
        if self.size() != other.size():
            raise ValueError()
        size = self.size()
        tmp = Matrix2D(size)
        for i in range(size[0]):
            for j in range(size[1]):
                tmp.matrix[i][j] += other.matrix[i][j] + self.matrix[i][j]
        return tmp

    def __sub__(self, other: "Matrix2D") -> "Matrix2D":
        if self.size() != other.size():
            raise ValueError()
        size = self.size()
        tmp = Matrix2D(size)
        for i in range(size[0]):
            for j in range(size[1]):
                tmp.matrix[i][j] += self.matrix[i][j] - other.matrix[i][j]
        return tmp

    def __mul__(self, other: "Matrix2D") -> "Matrix2D":
        if self.size() != other.size():
            raise ValueError()
        size = (self.size()[0], other.size()[1])
        midsize = self.size()[1]
        tmp = Matrix2D(size)
        for i in range(size[0]):
            for j in range(midsize):
                for k in range(size[1]):
                    tmp.matrix[i][k] += self.matrix[i][j] * other.matrix[j][k]
        return tmp

    def __str__(self) -> str:
        ml = max(max(len(str(i)) for i in j) for j in self.matrix) + 1
        return "\n".join(f"| {' '.join(f'{j:>{ml}}' for j in i)} |" for i in self.matrix)

    def __copy__(self) -> "Matrix2D":
        return self        

    def __deepcopy__(self, memodict={}) -> "Matrix2D":
        new = Matrix2D(matrix=self)
        memodict[id(new)] = new
        return new

"""
def gaussian_elimination(matrix):
    n = len(matrix); m = len(matrix[0]); no_mul = 0
    for i in range(n):
        pivot = matrix[i][i]
        for j in range(i+1,n):
            mul = -(matrix[j][i] / pivot); no_mul += 1
            for k in range(i,m):
                matrix[j][k] += mul * matrix[i][k]; no_mul += 1
    return matrix, no_mul

def solve_for_x(matrix):
    x = [float("inf")]*(len(matrix[0])-1); no_mul = 0
    for i in range(len(matrix)-1,-1,-1):
        ans = matrix[i][-1]
        for j in range(len(matrix[0])-2,len(matrix[0])-2-(len(matrix)-i)+1,-1):
            ans -= matrix[i][j] * x[j]; no_mul += 1
        x[i] = ans / matrix[i][i]; no_mul += 1
    return x, no_mul

hilbert_matrix = lambda size: [[1/(i+j+1) for i in range(size)] for j in range(size)]
"""