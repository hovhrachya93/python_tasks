# Write a recursive function to print each character of a string on a new line.

def printCharacters(s):
    if len(s) == 0:
       return
    print(s[0])
    printCharacters(s[1:])


if __name__ == "__main__":
    my_string = "hello"
    printCharacters(my_string)    
