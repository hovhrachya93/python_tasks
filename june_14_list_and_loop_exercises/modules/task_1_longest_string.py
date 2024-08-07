# TASK 1: Հայտարարել list, որը բաղկացած է string-ներից:
# Տպել list-ում եղած ամենաերկար string-ը և համապատասխան index-ը:
from typing import Union, Tuple, List


def findLongestString(lst: List[str]) -> Union[Tuple[str, int], None]:
    if not lst:
        return None
    max_string = max([(s, idx) for idx, s in enumerate(lst)], key=lambda x: len(x[0]))

    return max_string


if __name__ == "__main__":
    test_list = ["apple", "banana", "cherry"]
    print(f"In {test_list}, the longest string is and its index is: {findLongestString(test_list)}")

    empty_list = []
    print(f"In {empty_list}, the longest string is and its index is: {findLongestString(empty_list)}")
