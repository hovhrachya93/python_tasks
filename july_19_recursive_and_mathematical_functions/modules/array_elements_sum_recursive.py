# Write a recursive function to calculate
# the sum of all elements in a list.

def arrayElementsSumRecursive(arr):
   if len(arr) == 0:
        return 0
   return arr[0] + arrayElementsSumRecursive(arr[1:])

if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5]
    print("Sum of Elements:", arrayElementsSumRecursive(test_list))
