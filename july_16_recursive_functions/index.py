from fibonacci import fibonacci
from factorial import factorial
from list_length import listLength
from palindrome import isPalindrome
from sum_of_digits import sumOfDigits
from reverse_string import reverseString
from print_characters import printCharacters
from print_list_elements import printListElements
from sum_first_natural_numbers import sumFirstNaturalNumbers
from print_numbers import printNumbersUpwards, printNumbersDownwards

num = 15
string = "Hello, world!"
PalindromeString = "level"
list = [1, 2, 3, 2, 4, 2, 5, 3,7, 15, 1, 5]

print("Printing numbers upwards:")
printNumbersUpwards(1, 5)

print("Printing numbers downwards:")
printNumbersDownwards(5, 1)

print(f"Factorial of {num} is: {factorial(num)}")

print(f"Sum of the first {num} natural numbers: {sumFirstNaturalNumbers(num)}")

print("Printing all elements of the list recursively:")
printListElements(list)

print(f"List length is: {listLength(list)}")

print(f"The {num}th Fibonacci number is:", fibonacci(num))

print(f"Reversed '{string}' string is: {reverseString(string)}")

print("Print each character of a string on a new line")
printCharacters(string)

if isPalindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is NOT a palindrome.")

print(f"The sum of digits of {num} is:", sumOfDigits(num))