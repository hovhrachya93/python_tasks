from typing import List

docstringOfRotateMatrix180 = """
Rotate a square matrix by 180 degrees in place.

Args:
matrix (List[List[int]]): A 2D list (square matrix) to be rotated in place.
"""

def rotateMatrix180(matrix: List[List[int]]) -> None:
    """
    {docstringOfRotateMatrix180}
    """
    n = len(matrix)
    matrix.reverse()
    for i in range(n):
        matrix[i].reverse()

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("Original matrix:")
    for row in matrix:
        print(row)

    rotateMatrix180(matrix)
    
    print("\nMatrix after 180-degree rotation:")
    for row in matrix:
        print(row)

