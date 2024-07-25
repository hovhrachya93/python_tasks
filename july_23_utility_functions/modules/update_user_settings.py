# Create a function that updates user settings by passing keyword arguments dynamically.
# Use **kwargs to accept dynamic user settings.
# Use a function to pass these settings as keyword arguments to another function.

def updateUserSettings(**settings):
    return f"Settings applied: {settings}"

if __name__ == "__main__":
    settings = {'theme': 'dark', 'notifications': 'enabled'}
    print(updateUserSettings(**settings))
