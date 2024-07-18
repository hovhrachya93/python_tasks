# Write a recursive function to print all elements of a list.

def printListElements(lst):
    if not lst:
        return
    print(lst[0])
    printListElements(lst[1:])


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print("Printing all elements of the list recursively:")
    printListElements(my_list)