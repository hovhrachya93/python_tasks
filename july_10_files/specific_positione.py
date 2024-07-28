# Create a Python script that generates a text file named specific_position.txt. 
# Open the file in read and write mode ('r+'). Write some text at a specific position in the file.
#  If the file does not exist, create it first with some initial text.

fileName ="specific_position.txt"
writeMode = "r+"
initialText = "initial Text,"
text="Hello, world!"
position = len(initialText)

# try:
#     with open(fileName, writeMode) as fs:
#                 fs.seek(position)
#                 fs.write(" "+text)
#                 print(f"Text '{text}' written at position {position}")
# except FileNotFoundError:
#     with open(fileName, 'w') as fs:
#              fs.write(initialText)
#              print(f"File '{fileName}' created with initialText '{initialText.strip()}'")

fs = None
try:
    fs = open(fileName, writeMode)
    fs.seek(position)
    fs.write(" " + text)
    print(f"Text '{text}' written at position {position}")
except FileNotFoundError:
    try:
        fs = open(fileName, 'w')
        fs.write(initialText)
        print(f"File '{fileName}' created with initialText '{initialText.strip()}'")
    except Exception as e:
        print(f"Error creating file: {e}")
except Exception as e:
    print(f"Error writing to file: {e}")
finally:
    if fs is not None:
        fs.close()
        print('File closed!')