from typing import List

docstringOfTransposeMatrix = """
Transpose a given matrix.

Args:
matrix (List[List[int]]): A 2D list (matrix) to be transposed.

Returns:
List[List[int]]: The transposed matrix.
"""

docstringOfTransposeSquareMatrix = """
Transpose a given square matrix in place.

Args:
matrix (List[List[int]]): A 2D list (square matrix) to be transposed in place.
"""

def transposeMatrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    {docstringOfTransposeMatrix}
    """
    row_length = len(matrix)
    col_length = len(matrix[0])
    transpose_matrix = [[0] * row_length for _ in range(col_length)]
    for i in range(row_length):
        for j in range(col_length):
            transpose_matrix[j][i] = matrix[i][j]
    return transpose_matrix

def transposeSquareMatrix(matrix: List[List[int]]) -> None:
    """
    {docstringOfTransposeSquareMatrix}
    """
    size = len(matrix)
    for i in range(size):
        for j in range(i + 1, size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]

    square_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Original matrix:")
    for row in matrix:
        print(row)

    transposed_matrix = transposeMatrix(matrix)
    print("\nMatrix after transpose:")
    for row in transposed_matrix:
        print(row)

    print("\nOriginal square matrix:")
    for row in square_matrix:
        print(row)

    transposeSquareMatrix(square_matrix)
    print("\nSquare matrix after transpose:")
    for row in square_matrix:
        print(row)