# Իրականացնել ֆունկցիա, որը ստանում է list և
# վերադարձնում list-ի ամենափոքր (ամենամեծ) էլեմենտը։

def findMinMax(lst):
    if not lst:
        return None, None

    min_element = lst[0]
    max_element = lst[0]

    for num in lst:
        if num < min_element:
            min_element = num
        if num > max_element:
            max_element = num

    return min_element, max_element

if __name__ == '__main__':
    list = [3, 5, 1, 9, 2]
    min_element, max_element = findMinMax(list)
    print(f"Minimum element in {list} is:", min_element)
    print(f"Maximum element in {list} is:", max_element)
