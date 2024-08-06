# Task 1: Հայտարարել list, և տպել list-ի էլեմենտներից առավելագույնի արժեքը:
# List-ը պետք է պարունակի միայն int տիպի արժեքներ: Չօգտագործել max ֆունկցիան:
from typing import List

def find_max_value(lst: List[int]) -> int:
    if len(lst) == 0:
        return -1
    max_value = lst[0]
    for element in lst[1:]:
        if element > max_value:
            max_value = element
    return max_value


if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print('Maximum value in list:', find_max_value(sample_list))
