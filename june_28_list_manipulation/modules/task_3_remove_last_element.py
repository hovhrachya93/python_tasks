# TASK 3: Write a program that removes and returns the last element of
# a list without using the pop() method. If the list is empty,
# return a message indicating it is empty. Example usage on [1, 2, 3]
# should return 3 and the list becomes [1, 2].
from typing import Union, Tuple, List


def removeLastElement(lst: List[int]) -> Tuple[Union[int, str], List[int]]:
    if lst:
        return lst[-1], lst[:-1]
    else:
        return "List is empty.", lst


if __name__ == "__main__":
    test_list_empty = [1, 2, 3]
    removed_element, updated_list = removeLastElement(test_list_empty)
    print(f"Removed element: {removed_element}")
    print(f"Updated list: {updated_list}")

    test_list_empty = []
    removed_element, updated_list = removeLastElement(test_list_empty)
    print(f"Removed element: {removed_element}")
    print(f"Updated list: {updated_list}")
