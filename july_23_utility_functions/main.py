from modules import *

def main():
    # Greet a user with their full name and a custom message.
    print("Greeting 1:", greetUser("John", "Doe"))
    print("Greeting 2:", greetUser("Jane", "Smith", message="Welcome"))

    # Calculate the total price of items in a shopping cart, including tax.
    prices = [10.0, 20.0, 30.0]
    print("Total Price 1:", calculateTotalPrice(*prices))
    print("Total Price 2:", calculateTotalPrice(*prices, taxRate=0.07))

    # Print a user profile with name, age, and city.
    print(printUserProfile("John", "Doe", age=30, city="New York"))

    # Process data with different operations (sum, average, max, min).
    data = [1, 2, 3, 4, 5]
    print("Sum of Data:", processData(*data))
    print("Average of Data:", processData(*data, operation='average'))
    print("Max of Data:", processData(*data, operation='max'))
    print("Min of Data:", processData(*data, operation='min'))

    # Display product details by unpacking a dictionary.
    product = {'name': 'Laptop', 'price': 999.99, 'brand': 'BrandX'}
    print(displayProductDetails(**product))

    # Generate a report with both required and optional sections.
    print(generateReport("Monthly Report", "This is the content of the report."))
    print(generateReport("Annual Report", "This is the content of the report.", footer="Footer Text"))

    # Log messages with varying levels of severity and optional metadata.
    print(logMessages("Info: Application started.", "Warning: Low disk space.", level="DEBUG", timestamp="2024-07-25T12:00:00"))

    # Update user settings by passing keyword arguments dynamically.
    settings = {'theme': 'dark', 'notifications': 'enabled'}
    print(updateUserSettings(**settings))

if __name__ == "__main__":
    main()
