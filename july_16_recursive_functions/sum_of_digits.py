# Recursive function to find the sum of digits of a number.

def sumOfDigits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sumOfDigits(n // 10)


if __name__ == "__main__":
    number = 12345
    print(f"The sum of digits of {number} is:", sumOfDigits(number))