# Python File Handling Scripts

This repository contains four Python scripts demonstrating different file handling operations. Below is a brief description of each script and its functionality.

## Scripts Overview

### 1. `append_mode.py`

This script creates or opens a text file named `append_mode.txt` in append mode and writes a line of text to it. If the file already exists, the new text is added at the end.

### 2. `exclusive_mode.py`

This script creates a text file named `exclusive_mode.txt` in exclusive creation mode (`x`) and writes a line of text to it. If the file already exists, the script raises a `FileExistsError`.

### 3. `specific_position.py`

This script creates or opens a text file named `specific_position.txt` in read and write mode (`r+`). It writes text at a specific position in the file. If the file does not exist, it creates the file first with some initial text.

### 4. `word_occurrence_counter.py`

This script processes a given text file named `sample.txt` to find and count the occurrences of specific words. The words to be counted are: “example”, “all”, “word”, “up”, “did”, “him”.

## Usage

1. **Append Mode Script:**
   - Run `python append_mode.py` to append "Hello World!" to `append_mode.txt`.

2. **Exclusive Mode Script:**
   - Run `python exclusive_mode.py` to create `exclusive_mode.txt` and write "Hello, world!" to it. If the file exists, an error will be raised.

3. **Specific Position Script:**
   - Run `python specific_position.py` to write "Hello, world!" at a specific position in `specific_position.txt`. If the file does not exist, it will be created with initial text.

4. **Word Occurrence Counter Script:**
   - Run `python word_occurrence_counter.py` to count the occurrences of specific words in `sample.txt`.