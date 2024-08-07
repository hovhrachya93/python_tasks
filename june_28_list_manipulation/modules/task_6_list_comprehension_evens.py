# TASK 6: Write a single line of Python using list comprehension to filter and
# create a list of even numbers from an existing list[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
# resulting in [2, 4, 6, 8, 10].

def listComprehensionEvens(lst: list[int]) -> list[int]:
    return [item for item in lst if (item % 2 == 0)]


if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Before filtering even numbers, the list is: {test_list}")
    evens = listComprehensionEvens(test_list)
    print(f"After filtering even numbers, the list is: {evens}")

