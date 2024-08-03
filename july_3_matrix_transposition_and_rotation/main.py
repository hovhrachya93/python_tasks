from modules import *

def main():
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

    # Transpose the matrix
    print("Original matrix:")
    for row in matrix:
        print(row)
    
    transposed_matrix = transposeMatrix(matrix)
    print("\nMatrix after transpose:")
    for row in transposed_matrix:
        print(row)

    # Transpose the square matrix in place
    print("\nOriginal square matrix:")
    for row in square_matrix:
        print(row)

    transposeSquareMatrix(square_matrix)
    print("\nSquare matrix after in-place transpose:")
    for row in square_matrix:
        print(row)

  # Rotate matrix 180 degrees
    print("\nOriginal matrix before 180-degree rotation:")
    for row in matrix:
        print(row)

    rotateMatrix180(matrix)
    print("\nMatrix after 180-degree rotation:")
    for row in matrix:
        print(row)


if __name__ == "__main__":
    main()
