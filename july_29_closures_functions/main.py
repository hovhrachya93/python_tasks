from modules import *

def main():
    # Demonstrate the counter function
    print("Counter demonstration:")
    counter = makeCounter()
    print("Initial counter value:", counter())
    print("Next counter value:", counter())
    print("Next counter value:", counter())
    
    # Demonstrate the multiplier functions
    print("\nMultiplier demonstration:")
    multiplyBy2 = makeMultiplierOf(2)
    multiplyBy5 = makeMultiplierOf(5)
    
    print("Multiplying by 2:")
    print(f"3 multiplied by 2 is: {multiplyBy2(3)}")
    print(f"7 multiplied by 2 is: {multiplyBy2(7)}")
    
    print("\nMultiplying by 5:")
    print(f"3 multiplied by 5 is: {multiplyBy5(3)}")
    print(f"7 multiplied by 5 is: {multiplyBy5(7)}")

if __name__ == "__main__":
    main()
