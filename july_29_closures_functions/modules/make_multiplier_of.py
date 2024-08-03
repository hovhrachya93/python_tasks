from typing import Callable

docstringOfMakeMultiplierOf = """
Create a multiplier function that multiplies its argument by a given number.

Args:
n (int): The number by which the function's argument will be multiplied.

Returns:
Callable[[int], int]: A function that takes an integer as input and returns its product with n.
"""

def makeMultiplierOf(n: int) -> Callable[[int], int]:
    """
    {docstringOfMakeMultiplierOf}
    """
    def multiplier(x: int) -> int:
        return x * n
    
    return multiplier

if __name__ == "__main__":
    multiplyBy2 = makeMultiplierOf(2)
    multiplyBy5 = makeMultiplierOf(5)
    
    print("Multiplying by 2:")
    print(f"3 multiplied by 2 is: {multiplyBy2(3)}")
    print(f"7 multiplied by 2 is: {multiplyBy2(7)}")
    
    print("\nMultiplying by 5:")
    print(f"3 multiplied by 5 is: {multiplyBy5(3)}")
    print(f"7 multiplied by 5 is: {multiplyBy5(7)}")


