# TASK 7: Մուտքագրել քառակուսային մատրից և տպել էկրանին նրա տարրերը։

def printMatrix(matrix: list[list[int]]) -> None:
    for row in matrix:
        print(' '.join(map(str, row)))


if __name__ == "__main__":
    test_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    printMatrix(test_matrix)
