# Իրականացնել ֆունկցիա, որն ընդունում է թիվ և 
# վերադարձնում նրա թվանշանների գումարը: (123 -> 1 + 2 + 3)

def sumOfDigits(n):
    totalSum = sum(int(digit) for digit in str(n))
    return totalSum

if __name__ == '__main__':
    num = int(input("Enter an integer to find the sum of its digits: "))
    print(f"Sum of digits of {num} is:", sumOfDigits(num))

