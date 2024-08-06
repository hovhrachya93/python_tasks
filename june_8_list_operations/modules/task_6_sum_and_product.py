# Task 6: Հայտարարել list և տպել բոլոր էլեմենտների գումարը, արտադրյալը:
# Չօգտագործել sum ֆունկցիան.
from typing import List, Tuple, Union


def sum_and_product(lst: List[Union[int, float]]) -> Tuple[Union[int, float], Union[int, float]]:
    if len(lst) == 0:
        return 0, 0

    total_sum = 0
    total_product = 1

    for element in lst:
        total_sum += element
        total_product *= element

    return total_sum, total_product


if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = sum_and_product(sample_list)
    print('Sum and product of elements in list:', result)
