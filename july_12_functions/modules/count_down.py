# Գրել ֆունկցիա, որը ստանում է n բնական թիվ և տպում է n-ից 0 թվերը։

def countDown(n):
    if(n<0):
        print("Please provide positive integer")
    for i in range(n, -1, -1):
        print("count down: ", i)

if __name__ == "__main__":
    n = int(input("Enter a positive integer for count down: "))
    countDown(n)
