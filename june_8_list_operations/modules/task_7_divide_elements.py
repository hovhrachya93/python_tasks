# Task 7: Հայտարարել list: List-ի բոլոր էլեմենտները փոխարինել այդ
# էլեմենտի արժեքը բաժանած list-ում էլեմենտների քանակի վրա։
from typing import List


def divide_elements(lst: List[float]) -> List[float]:
    length = len(lst)
    if length == 0:
        return []

    divided_list = [element / length for element in lst]

    return divided_list


if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print('List after dividing elements by length:', divide_elements(sample_list))
