# Write a recursive function to reverse a given string.

def reverseString(s):
    if len(s) == 0:
        return ''
    return s[-1] + reverseString(s[:-1])


if __name__ == "__main__":
    my_string = "hello World!"
    print("Reversed string:", reverseString(my_string))