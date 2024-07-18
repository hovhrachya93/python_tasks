# Write a recursive function to calculate the factorial of a given number.

def factorial(num):
    if(num == 0):
        return 1
    return num * factorial(num-1)


if __name__ == "__main__":
    number = 5
    print(f"Factorial of {number} is: {factorial(number)}")
