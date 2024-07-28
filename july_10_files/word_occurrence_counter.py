# Create a Python script that processes a given text file
# to find and count the occurrences of a specific word. 
# For this task, you will use a sample text file and count
# how many times the words “example”, “all”, “word”, “up”, “did”, “him” appear.

fileName = 'sample.txt'
words = ["example", "all", "word", "up", "did", "him"]
counts = {word: 0 for word in words}

try:
    with open(fileName, 'r') as fs:
           content=fs.read()

    for word in words:
            count = content
            count = content.count(word)
            counts[word] = count

    for word, count in counts.items():
        print(word + " : " + str(count))

except FileNotFoundError as e:
        print(f"File '{fileName}' not found.")
except Exception as e:
        print(f"An error occurred: {e}")