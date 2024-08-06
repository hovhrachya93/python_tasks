# Task 4: Հայտարարել list և տպել նվազագույն արժեքով էլեմենտի ինդեքսը։
from typing import List, Union


def find_min_index(lst: List[Union[int, float]]) -> int:
    if len(lst) == 0:
        return -1
    min_element_index = 0
    for i in range(1, len(lst)):
        if lst[i] < lst[min_element_index]:
            min_element_index = i
    return min_element_index


if __name__ == '__main__':
    sample_list = [1, 2.5, 0.9, 4.5]
    print('Index of minimum value in list:', find_min_index(sample_list))
