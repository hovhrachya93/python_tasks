# Create a function to calculate the total price of items in a shopping cart.
# Use positional-only arguments for item prices.
# Use a keyword argument for the tax rate with a default value.
# Return the total price including tax.

def calculateTotalPrice(*itemPrices, taxRate=0.08):
    subtotal = sum(itemPrices)
    total = subtotal * (1 + taxRate)
    return total

if __name__ == "__main__":
    prices = [10.0, 20.0, 30.0]
    print(f"Total Price 1: ${calculateTotalPrice(*prices):.2f}")
    print(f"Total Price 2: ${calculateTotalPrice(*prices, taxRate=0.07):.2f}")

