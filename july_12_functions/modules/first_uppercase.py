# Իրականացնել ֆունկցիա, որը ստանում է տող և 
# վերադարձնում տողում առաջին հանդիպած մեծատառը։

def printFirstUppercaseCharacter(s):
    for char in s:
        if char.isupper():
            print("First uppercase character:", char)
            return
    print("No uppercase character found.")

if __name__ == '__main__':
    with open('../documents/sample.txt', 'r') as file:
        string = file.read()
        printFirstUppercaseCharacter(string)