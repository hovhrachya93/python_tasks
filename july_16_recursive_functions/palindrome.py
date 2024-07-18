# Recursive function to check if a string is a palindrome.

def isPalindrome(s):
    if len(s) <=1:
        return True
    
    if s[0] == s[-1]:
        return isPalindrome(s[1:-1])
    else:
        return False
    

if __name__ == "__main__":
    string = "bob"
    
    if isPalindrome(string):
        print(f"'{string}' is a palindrome.")
    else:
        print(f"'{string}' is NOT a palindrome.")
