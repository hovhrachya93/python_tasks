from modules import *


def main():
    # Task 1
    my_list_1 = [1, 2, 4, 5]
    value_to_insert = 3
    index_to_insert = 1
    updated_list_1 = insertValue(my_list_1, value_to_insert, index_to_insert)
    print(f"After inserting {value_to_insert} at index {index_to_insert}, the list is: {updated_list_1}")

    # Task 2
    my_list_2 = [1, 2, 3, 2, 4]
    element_to_remove_2 = 2
    updated_list_2 = removeElement(my_list_2, element_to_remove_2)
    if updated_list_2 == my_list_2:
        print(f"The element {element_to_remove_2} is not found, so the list is unchanged: {updated_list_2}")
    else:
        print(f"After removing the first occurrence of {element_to_remove_2}, the list is: {updated_list_2}")

    # Task 3
    my_list_3 = [1, 2, 3]
    removed_element, updated_list = removeLastElement(my_list_3)
    print('Removed last element:', removed_element)
    print('Updated list:', updated_list)

    # Task 4
    my_list_4 = [1, 2, 3]
    test_list = [1, 2, 3]
    print(f"{my_list_4} list before clear")
    clearList(my_list_4)
    print(f"{my_list_4} list After clear")

    # Task 5
    print('List of squares from 1 to 10:', listComprehensionSquares())

    # Task 6
    existing_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Before filtering even numbers: {existing_list}")
    evens = listComprehensionEvens(existing_list)
    print(f"After filtering even numbers: {evens}")


if __name__ == '__main__':
    main()
