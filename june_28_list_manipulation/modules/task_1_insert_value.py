# TASK 1: Write a program that inserts a value at a specified index in
# a list without using the built-in insert() method. For example,
# insert the value 3 at index 1 in the list [1, 2, 4, 5] to make it [1, 3, 2, 4, 5].

def insertValue(lst: list[int], value: int, index: int) -> list[int]:
    return lst[:index] + [value] + lst[index:]


if __name__ == "__main__":
    test_list = [1, 2, 4, 5]
    value = 3
    index = 1
    result = insertValue(test_list, value, index)
    print(f"After inserting {value} at index {index}, the list is: {result}")
