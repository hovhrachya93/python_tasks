# Write a recursive function to find the sum of the first N natural numbers.

def sumFirstNaturalNumbers(n):
    if n == 1:
        return 1
    else:
        return n + sumFirstNaturalNumbers(n-1)


if __name__ == "__main__":
    num = 5
    print(f"Sum of the first {num} natural numbers: {sumFirstNaturalNumbers(num)}")