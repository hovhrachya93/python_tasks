# Create a function to greet a user with their full name and a custom message.
# Use positional arguments for first name and last name.
# Use a keyword argument for the greeting message with a default value.

def greetUser(first_name, last_name, message="Hello"):
    return f"{message}, {first_name} {last_name}!"

if __name__ == "__main__":
    print(greetUser("John", "Doe")) 
    print(greetUser("Jane", "Smith", message="Welcome"))
