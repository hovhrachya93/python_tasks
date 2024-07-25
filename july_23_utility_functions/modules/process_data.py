# Create a function to process data with different operations.
# Use positional-only arguments for data (list of numbers).
# Use a keyword argument for the operation (default is ‘sum’).
# Return the result of the operation.

def processData(*data, operation='sum'):
    if operation == 'sum':
        return sum(data)
    elif operation == 'average':
        return sum(data) / len(data) if data else 0
    elif operation == 'max':
        return max(data) if data else None
    elif operation == 'min':
        return min(data) if data else None
    else:
        raise ValueError("Unknown operation")

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print(f"Sum: {processData(*data)}")
    print(f"Average: {processData(*data, operation='average')}")
    print(f"Max: {processData(*data, operation='max')}")
    print(f"Min: {processData(*data, operation='min')}")
