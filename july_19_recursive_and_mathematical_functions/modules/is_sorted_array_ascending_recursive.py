# Write a recursive function to check if
# a list is sorted in ascending order.

def isSortedArrayAscendingRecursive(arr):
    if len(arr) <= 1:
        return True
    if arr[0] > arr[1]:
        return False
    return isSortedArrayAscendingRecursive(arr[1:])

if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5]
    print("Is Sorted Ascending:", isSortedArrayAscendingRecursive(test_list))
