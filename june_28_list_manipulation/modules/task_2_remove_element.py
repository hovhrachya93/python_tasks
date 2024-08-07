# TASK 2: Write a program that removes the first occurrence of a specified element from
# a list without using the remove() method. If the element does not exist, print a message.
# Example: Remove 2 from [1, 2, 3, 2, 4] resulting in [1, 3, 2, 4].

def removeElement(lst: list[int], element: int) -> list[int]:
    if element in lst:
        return [item for item in lst if item != element or (item == element and not (element := None))]
    else:
        print(f"Element {element} not found in list.")
        return lst


if __name__ == "__main__":
    test_list = [1, 2, 3, 2, 4]
    element_to_remove = 8
    updated_list = removeElement(test_list, element_to_remove)
    if updated_list == test_list:
        print(f"The element {element_to_remove} is not found, so the list is unchanged: {updated_list}")
    else:
        print(f"After removing the first occurrence of {element_to_remove}, the list is: {updated_list}")
