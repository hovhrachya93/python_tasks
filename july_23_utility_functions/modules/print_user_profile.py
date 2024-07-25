# Create a function to print a user profile.
# Use keyword-only arguments for age and city.
# Use positional arguments for first name and last name.

def printUserProfile(first_name, last_name, *, age, city):
    return f"Name: {first_name} {last_name}, Age: {age}, City: {city}"

if __name__ == "__main__":
    print(printUserProfile("John", "Doe", age=30, city="New York"))
