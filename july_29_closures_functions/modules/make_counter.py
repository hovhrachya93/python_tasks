from typing import Callable

docstringOfMakeCounter = """
Create a counter function that starts at 0 and increments by 1 each time it is called.

Returns:
Callable[[], int]: A function that, when called, returns the next value in the counter sequence.
"""

def makeCounter() -> Callable[[], int]:
    """
    {docstringOfMakeCounter}
    """
    count = 0
    
    def counter() -> int:
        nonlocal count
        count += 1
        return count - 1
    
    return counter


if __name__ == "__main__":
    counter = makeCounter()
    print("Initial counter value:", counter())
    print("Next counter value:", counter())
    print("Next counter value:", counter())
