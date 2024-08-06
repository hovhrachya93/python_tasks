# Task 2: Հայտարարել list, և տպել list-ի էլեմենտներից նվազագույնի արժեքը:
# List-ը պետք է պարունակի միայն int և float տիպի էլեմենտներ: Չօգտագործել min ֆունկցիան:
from typing import List, Union

def find_min_value(lst: List[Union[int, float]]) -> Union[int, float]:
    if len(lst) == 0:
        return -1
    min_value = lst[0]
    for element in lst[1:]:
        if element < min_value:
            min_value = element
    return min_value


if __name__ == '__main__':
    sample_list = [2.2, 5, 3.3, 4.4, 5.5, 1.1]
    print('Minimum value in list:', find_min_value(sample_list))
