from modules import *

def main():
    # Print numbers from n to 0
    n = int(input("Enter a positive integer for count down: "))
    countDown(n)
    
    # Print numbers from 0 to n
    n = int(input("Enter a positive integer for count up: "))
    countUp(n)

    # Find the first uppercase character in a string
    with open('./documents/sample.txt', 'r') as file:
        string = file.read()
        printFirstUppercaseCharacter(string)

    # Find the minimum and maximum elements in a list
    list = [3, 5, 1, 9, 2]
    min_element, max_element = findMinMax(list)
    print(f"Minimum element in {list} is:", min_element)
    print(f"Maximum element in {list} is:", max_element)

    # Print elements of a list
    list_to_print = [1, 2, 3]
    print("Elements of the list:")
    printListElement(list_to_print)

    # Calculate the sum of digits of a number
    num = int(input("Enter an integer to find the sum of its digits: "))
    print(f"Sum of digits of {num} is:", sumOfDigits(num))

if __name__ == "__main__":
    main()
