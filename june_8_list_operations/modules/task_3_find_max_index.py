# Task 3: Հայտարարել list և տպել առավելագույն արժեքով էլեմենտի ինդեքսը։
from typing import List


def find_max_index(lst: List[int]) -> int:
    if len(lst) == 0:
        return -1
    max_element_index = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[max_element_index]:
            max_element_index = i
    return max_element_index


if __name__ == '__main__':
    sample_list = [1, 2, 5, 3, 4]
    print('Index of maximum value in list:', find_max_index(sample_list))
