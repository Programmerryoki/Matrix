from typing import List, Tuple


class Matrix:
    matrix = None
    _size = None

    def __init__(self, size: Tuple[int] = None,
                 matrixlist: List[List[int]] = None,
                 matrix: "Matrix" = None,
                 **kwargs):
        if size:
            self._size = size

    def size(self) -> Tuple[int]:
        return self._size()

    def __eq__(self, other: "Matrix") -> bool:


    def __bool__(self) -> bool:
        return bool(self.size() and self.matrix)

    def __add__(self, other: "Matrix") -> "Matrix":

    def __sub__(self, other: "Matrix") -> "Matrix":

    def __mul__(self, other: "Matrix") -> "Matrix":

    def __str__(self) -> str:
        ml = max(max(len(str(i)) for i in j) for j in self.matrix) + 1
        return "\n".join(f"| {' '.join(f'{j:>{ml}}' for j in i)} |" for i in self.matrix)

    def __copy__(self) -> "Matrix":
        return self

    def __deepcopy__(self, memodict={}) -> "Matrix":
        new = Matrix(matrix=self)
        memodict[id(new)] = new
        return new
