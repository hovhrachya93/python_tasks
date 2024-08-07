# TASK 4: Develop a program that clears all elements from
# a list without using the `clear()` method.
# After running the function on `[1, 2, 3]`, the list should be empty.

def clearList(lst: list[int]) -> None:
    while lst:
        lst.pop()


if __name__ == "__main__":
    test_list = [1, 2, 3]
    print(f"{test_list} list before clear")
    clearList(test_list)
    print(f"{test_list} list After clear")

