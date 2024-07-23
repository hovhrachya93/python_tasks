from modules import (
    isPowerOfTwo,
    isPrimeNumber,
    firstNFibonacci,
    findMaxOfThreeNumbers,
    flattenListRecursively,
    arrayElementsSumRecursive,
    isSortedArrayAscendingRecursive
)

def main():
    print("Flatten List:", flattenListRecursively([1, [2, [3, 4], 5], 6, [7, 8]]))
    print("Sum of Elements:", arrayElementsSumRecursive([1, 2, 3, 4, 5]))
    print("Is Sorted Ascending:", isSortedArrayAscendingRecursive([1, 2, 3, 4, 5]))
    print("Is Prime:", isPrimeNumber(29))
    print("Max of Three Numbers:", findMaxOfThreeNumbers(5, 10, 7))
    print("First N Fibonacci Numbers:", firstNFibonacci(7))
    print("Is Power of Two:", isPowerOfTwo(16))

if __name__ == "__main__":
    main()
