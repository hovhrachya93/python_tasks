# Create a Python script that generates a text file named exclusive_mode.txt. 
# Open the file in exclusive creation mode ('x') and write some text into it.
#  If the file already exists, the script should raise a FileExistsError.

fileName = "exclusive_mode.txt"
writeMode = "x"
text="Hello, world!"

# try:
#      with open(fileName, writeMode) as fs:
#         fs.write(text+"\n")
#         print("File created")
# except FileExistsError:
#       print('File exists!')
# except Exception as e:
#      print(e)

fs = None
try:
     fs = open(fileName,  writeMode)
     fs.write(text+"\n")
     print("File created")
except FileExistsError:
     print('File exists!')
except Exception as e:
     print(e)
finally:
       if fs is not None:
            fs.close()
            print('File closed!')