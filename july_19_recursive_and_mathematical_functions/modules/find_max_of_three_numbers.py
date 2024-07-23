# Write a function that takes three numbers as input
# and returns the maximum of the three.

def findMaxOfThreeNumbers(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c

if __name__ == "__main__":
    a, b, c = 5, 10, 7
    print("Max of Three Numbers:", findMaxOfThreeNumbers(a, b, c))
