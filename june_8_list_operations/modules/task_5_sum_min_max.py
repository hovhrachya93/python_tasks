# Task 5: Հայտարարել list և տպել նվազագույն և առավելագույն արժեքներով էլեմենտների գումարը:
from typing import List, Union


def sum_min_max(lst: List[Union[int, float]]) -> Union[int, float]:
    if len(lst) == 0:
        return -1
    min_value = lst[0]
    max_value = lst[0]
    for value in lst[1:]:
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value
    return min_value + max_value


if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print('Sum of minimum and maximum values in list:', sum_min_max(sample_list))
