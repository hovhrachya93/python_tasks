# Write a recursive function to print numbers from 5 to 1.

def printNumbersUpwards(start, end):
    if(start <= end):
        print(start)
        printNumbersUpwards(start + 1, end)

# Write a recursive function to print numbers from 5 to 1.
def printNumbersDownwards(start, end):
    if(start>=end):
        print(start)
        printNumbersDownwards(start - 1, end)


if __name__ == "__main__":
    print("Printing numbers upwards:")
    printNumbersUpwards(1, 5)

    print("Printing numbers downwards:")
    printNumbersDownwards(5, 1)