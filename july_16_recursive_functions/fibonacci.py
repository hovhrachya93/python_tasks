# Write a recursive function to generate the Nth Fibonacci number.

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    num = 10 
    print(f"The {num}th Fibonacci number is: ", fibonacci(num))