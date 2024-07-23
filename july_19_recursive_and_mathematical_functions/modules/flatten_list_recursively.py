# Write a recursive function to flatten a list that may contain nested lists.
# For example: nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
# flattened = flattenListRecursively(nested_list)  # [1, 2, 3, 4, 5, 6, 7, 8]

def flattenListRecursively(nested_list):
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flattenListRecursively(item))
        else:
            flattened.append(item)
    return flattened

if __name__ == "__main__":
    test_list = [1, [2, [3, 4], 5], 6, [7, 8]]
    print("Flattened List:", flattenListRecursively(test_list))
