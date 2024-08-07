# Python List Manipulation

This project includes implementations for a series of tasks involving list operations in Python. Each task is defined in separate Python files and demonstrates different aspects of working with lists, including inserting values, removing elements, clearing lists, and using list comprehensions.

## Files

- **`task_1_insert_value.py`**: Contains a function to insert a value at a specified index in a list without using the built-in `insert()` method.
- **`task_2_remove_element.py`**: Contains a function to remove the first occurrence of a specified element from a list without using the `remove()` method. If the element does not exist, a message is printed.
- **`task_3_remove_last_element.py`**: Contains a function to remove and return the last element of a list without using the `pop()` method. If the list is empty, a message is returned indicating it is empty.
- **`task_4_clear_list.py`**: Contains a function to clear all elements from a list without using the `clear()` method. After running the function, the list should be empty.
- **`task_5_list_comprehension_squares.py`**: Contains a function to generate a list of squares for all integers from 1 to 10 using list comprehension. The resulting list should be `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`.
- **`task_6_list_comprehension_evens.py`**: Contains a function to create a list of even numbers from an existing list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` using list comprehension. The resulting list should be `[2, 4, 6, 8, 10]`.

## Running the Code

To run all tasks, execute the `main.py` script:

```bash
python main.py
```
To run individual tasks directly, navigate to the modules directory and execute the desired file:

```bash
cd modules
python <<File name>>.py
```