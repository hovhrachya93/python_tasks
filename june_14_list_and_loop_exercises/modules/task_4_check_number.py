# TASK 4: Գրել ծրագիր, որը ստանում է ամբողջ թիվ։ Հայտարարել list:
# Եթե list-ում առկա է տրված թիվը տպել YES, հակառակ դեպքում տպել NO։

def checkNumberInList(numbers: list[int], number: int) -> str:
    if number in numbers:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5]

    test_number = 3
    result = checkNumberInList(test_list, test_number)
    print(f"{result} there is {'no ' if result == 'NO' else ''}{test_number} in {test_list}")

    test_number = 6
    result = checkNumberInList(test_list, test_number)
    print(f"{result} there is {'no ' if result == 'NO' else ''}{test_number} in {test_list}")
