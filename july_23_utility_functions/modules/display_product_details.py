# Create a function to display product details by unpacking a dictionary.
# Use unpacking to pass product details as keyword arguments to the function.

def displayProductDetails(name, price, brand):
    return f"Product Name: {name}, Price: ${price:.2f}, Brand: {brand}"

if __name__ == "__main__":
    product = {'name': 'Laptop', 'price': 999.99, 'brand': 'BrandX'}
    print(displayProductDetails(**product))
