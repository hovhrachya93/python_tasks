# TASK 5: Use list comprehension to generate a list of squares for all integers
# from 1 to 10. The resulting list should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].

def listComprehensionSquares() -> list[int]:
    return [item * item for item in range(1, 11)]


if __name__ == "__main__":
    print(listComprehensionSquares())
