# Write a function that takes an integer n 
# and returns a list of the first n Fibonacci numbers.

def firstNFibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    else:
        fib=firstNFibonacci(n-1)
        return fib + [fib[-1] + fib[-2]]

if __name__ == "__main__":
    n = 7
    print("First N Fibonacci Numbers:", firstNFibonacci(n))
