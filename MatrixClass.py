from typing import List


class Matrix:
    matrix = None

    def __init__(self, size : (int, int) = (1,1),
                 arraymatrix : List[List[int]] = None,
                 matrix : "Matrix" = None):
        self.matrix = [[0]*size[0] for _ in range(size[1])]

    def size(self) -> (int, int):
        return len(self.matrix), len(self.matrix[0])

    def __add__(self, other) -> "Matrix":
        if self.size() != other.size():
            raise ValueError()
        size = self.size()
        tmp = Matrix(size)
        for i in range(size[0]):
            for j in range(size[1]):
                tmp.matrix[i][j] += other.matrix[i][j] + self.matrix[i][j]
        return tmp

    def __mul__(self, other) -> "Matrix":
        if self.size() != other.size():
            raise ValueError()
        size = (self.size()[0], other.size()[1])
        midsize = self.size()[1]
        tmp = Matrix(size)
        for i in range(size[0]):
            for j in range(midsize):
                for k in range(size[1]):
                    tmp.matrix[i][k] += self.matrix[i][j] * other.matrix[j][k]
        return tmp

    def __str__(self):
        ml = max(max(len(str(i)) for i in j) for j in self.matrix) + 1
        return "\n".join(f"| {' '.join(f'{j:>{ml}}' for j in i)} |" for i in self.matrix)


A = Matrix()
A.matrix = [[1,0,0],[0,1,0],[0,0,1]]
B = Matrix()
B.matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print((A * B).matrix)
print((A * B))

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
theoretical_no_of_mul = lambda n: round(n**3/3 + n**2 - n/3)
for size in [5,11,12,13]:
    no_of_mul = 0
    H = hilbert_matrix(size); b = [[sum(i)] for i in H]
    system, tmp = gaussian_elimination([H[i]+b[i] for i in range(len(H))])
    no_of_mul += tmp
    solution, tmp = solve_for_x(system)
    no_of_mul += tmp
    error = [abs(1.0-i) for i in solution]
    print(f"Solving Hilbert Matrix of size {size}:",end="\t\t")
    print(f"Transpose of Exact Solution: [{', '.join('1' for _ in range(len(solution)))}]")
    print(f"Transpose of Computed Solution: [{','.join(map(lambda x: f'{x:>8.4f}', solution))}]")
    print(f"Error : [{','.join(map(lambda x: f'{x:>8.4f}', error))}]")
    print(f"Infinity Norm: {max(abs(i) for i in error):>8.4f}")
    print(f"Euclidean Norm: {(sum(i**2 for i in error))**0.5:>8.4f}")
    print(f"Number of multiplications in my computer program = {no_of_mul}")
    print(f"Number of multiplications for n={size}, using the formula in our book, my answer should have been: {theoretical_no_of_mul(size)}")
    print()
"""