# Write a function in Python that determines whether a given number 
# is a power of 2. A number is considered a power of 2 if it 
# can be expressed as 2^k, where k is a non-negative integer.

def isPowerOfTwo(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

if __name__ == "__main__":
    test_number = 16
    print("Is Power of Two:", isPowerOfTwo(test_number))
