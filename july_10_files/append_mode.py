# Create a Python script that generates a text file named append_mode.txt.
# Open the file in append mode and write some text into it. If the file 
# already exists, the new text should be added at the end of the file.

fileName = 'append_mode'
writeMode = 'a'
text = 'Hello World!'

try:
    with open(fileName + '.txt', writeMode) as fs:
        fs.write(text + '\n');
except Exception as e:
            print(e)

# try:
#        fs = open(fileName + '.txt', 'a')
#        fs.write(text + '\n');
# except Exception as e:
#        print(e)
# finally:
#        if(fs):
#             fs.close()
#             print('File closed!')
