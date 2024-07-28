# Գրել ֆունկցիա, որը ստանում է list և տպում է list-ի էլեմենտները էկրանին։

def printListElement(list):
    for element in list:
        print(element)

if __name__ == '__main__':
    list = [1, 2, 3]
    print("Elements of the list:")
    printListElement(list)