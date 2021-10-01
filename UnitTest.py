import unittest
from copy import copy, deepcopy

from MatrixClass import Matrix2D

class TestMatrix2D(unittest.TestCase):
    def test_initializer_size(self):
        A = Matrix2D((1,1))
        self.assertEqual(A.matrix, [[0]])

    def test_initializer_matrixlist(self):
        matlist = [[1,2],[3,4]]
        A = Matrix2D(matrixlist=matlist)
        self.assertEqual(A.matrix, matlist)

    def test_initializer_matrix(self):
        A = Matrix2D(matrixlist=[[1,2],[3,4]])
        B = Matrix2D(matrix=A)
        self.assertEqual(A, B)

    def test_size(self):
        A = Matrix2D(matrixlist=[[1,2,3]])
        self.assertEqual(A.size(), (1,3))

    def test_equal(self):
        tmp = [[1,2,3],[4,5,6]]
        A = Matrix2D(matrixlist=tmp)
        B = Matrix2D(matrixlist=tmp)
        self.assertEqual(A, B)

    def test_addition(self):
        A = Matrix2D(matrixlist=[[1,2],[3,4]])
        B = Matrix2D(matrixlist=[[2,3],[4,5]])
        ans = Matrix2D(matrixlist=[[3,5],[7,9]])
        self.assertEqual(A+B, ans)

    def test_subtraction(self):
        A = Matrix2D(matrixlist=[[2,3],[4,5]])
        B = Matrix2D(matrixlist=[[1,2],[3,4]])
        ans = Matrix2D(matrixlist=[[1,1],[1,1]])
        self.assertEqual(A-B, ans)

    def test_multiplication(self):
        A = Matrix2D(matrixlist=[[1,2],[3,4]])
        B = Matrix2D(matrixlist=[[2,3],[4,5]])
        ans = Matrix2D(matrixlist=[[10,13],[22,29]])
        self.assertEqual(A*B, ans)

    def test_string_output(self):
        A = Matrix2D(matrixlist=[[1,2,3],[4,5,6]])
        self.assertMultiLineEqual(str(A), "|  1  2  3 |\n|  4  5  6 |")

    def test_copy(self):
        A = Matrix2D(matrixlist=[[1,2],[3,4]])
        self.assertIs(A, copy(A))

    def test_deepcopy(self):
        A = Matrix2D(matrixlist=[[1,2],[3,4]])
        self.assertEqual(A, deepcopy(A))


if __name__ == '__main__':
    unittest.main()