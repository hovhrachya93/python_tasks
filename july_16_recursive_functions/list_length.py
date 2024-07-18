# Write a recursive function to find the length of a list.

def listLength(lst):
    if not lst:
        return 0
    return 1 + listLength(lst[1:])


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print("Length of the list:", listLength(my_list))
