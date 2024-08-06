from modules import *

def main():
    sample_list_int = [1, 2, 3, 4, 5]
    sample_list_float = [1.1, 2.2, 3.3, 4.4, 5.5]

    # Task 1
    print('Maximum value in list:', find_max_value(sample_list_int))

    # Task 2
    print('Minimum value in list:', find_min_value(sample_list_float))

    # Task 3
    print('Index of maximum value in list:', find_max_index(sample_list_int))

    # Task 4
    print('Index of minimum value in list:', find_min_index(sample_list_int))

    # Task 5
    print('Sum of minimum and maximum values in list:', sum_min_max(sample_list_int))

    # Task 6
    print('Sum and product of elements in list:', sum_and_product(sample_list_int))

    # Task 7
    print('List after dividing elements by length:', divide_elements(sample_list_int))

    # Task 8
    input_list_elements()


if __name__ == '__main__':
    main()
