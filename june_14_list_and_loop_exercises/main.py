from modules import *


def main():
    # Task 1
    sample_list_1 = ["apple", "banana", "cherry"]
    longest_string, longest_index = findLongestString(sample_list_1)
    print(f'In {sample_list_1}, the longest string is "{longest_string}" at index {longest_index}')

    # Task 2
    sample_list_2 = ["tom", "jane", "ann"]
    capitalized_list = capitalizeFirstLetters(sample_list_2)
    print(f'{sample_list_2} list with capitalized first letters: {capitalized_list}')

    # Task 3
    sample_list_3 = [1, "apple", 3.5, True]
    print(f"{sample_list_3} in reverse is {sample_list_3}")

    # Task 4
    sample_list_4 = [1, 2, 3, 4, 5]
    
    test_number_4 = 3
    result = checkNumberInList(sample_list_4, test_number_4)
    print(f"{result} there is {'no ' if result == 'NO' else ''}{test_number_4} in {sample_list_4}")
    
    test_number_4 = 6
    result = checkNumberInList(sample_list_4, test_number_4)
    print(f"{result} there is {'no ' if result == 'NO' else ''}{test_number_4} in {sample_list_4}")

    # Task 5
    sample_list_5 = ["apple", "banana", "apple", "cherry", "banana"]
    occurrences = countStringOccurrences(sample_list_5)
    print('String occurrences in list:', occurrences)

    # Task 6
    sample_list_6 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    partitioned_list = partitionEvenOdd(sample_list_6)
    print('Partitioned list with evens first and odds later:', partitioned_list)

    # Task 7
    sample_matrix_7 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print('Matrix elements:')
    printMatrix(sample_matrix_7)


if __name__ == '__main__':
    main()
