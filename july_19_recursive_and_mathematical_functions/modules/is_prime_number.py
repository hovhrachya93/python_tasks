# Write a function that takes an integer as input
# and returns True if the number is prime, False otherwise.

def isPrimeNumber(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    test_number = 29
    print("Is Prime:", isPrimeNumber(test_number))
