# Write a function to log messages with varying levels of severity.
# Use *args to handle an arbitrary number of messages.
# Use **kwargs to handle keyword arguments for metadata (like timestamp, user, etc.).

def logMessages(*messages, **metadata):
    log = "\n".join(messages)
    for key, value in metadata.items():
        log += f"\n{key}: {value}"
    return log

if __name__ == "__main__":
    print(logMessages("Info: Application started.", "Warning: Low disk space.", level="DEBUG", timestamp="2024-07-25T12:00:00"))
