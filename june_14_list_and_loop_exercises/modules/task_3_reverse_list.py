# TASK 3: Հայտարարել list և տպել list-ի էլեմենտները հակառակ հերթականությամբ:
# List-ը կարող է պարունակել ցանկացած տիպի էլեմենտ:

def printReversedList(lst: list) -> list:
    return lst[::-1]


if __name__ == "__main__":
    test_list = [1, "apple", 3.5, True]
    print(f"{test_list} in reverse is {printReversedList(test_list)}")
