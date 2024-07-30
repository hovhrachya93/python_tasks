#Գրել ֆունկցիա, որը ստանում է n բնական թիվ և տպում է 0-ից n թվերը։

def countUp(n):
    if(n<0):
        print("Please provide positive integer")
        return
    for i in range(0, n+1):
        print(f"Count up: {i}")

if __name__ == "__main__":
    n = int(input("Enter a positive integer for count up: "))
    countUp(n)