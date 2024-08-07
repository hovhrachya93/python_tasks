# TASK 6: Գրեք ծրագիր, որը ամբողջ թվային զանգվածի բոլոր զույգ էլեմենտները
# կտեղավորի նույն զանգվածի մեջ սկզբից, իսկ կենտերը՝ վերջից:

def partitionEvenOdd(numbers: list[int]) -> list[int]:
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return even_numbers + odd_numbers


if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(partitionEvenOdd(test_list))
