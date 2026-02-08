# Python File Handling Assignment

This repository contains Python scripts demonstrating basic file operations, including reading, writing, appending, and error handling. These tasks were completed as part of a Python programming assignment.

## Project Structure

* `task1_read_handle.py`: A script that reads a text file line-by-line and handles `FileNotFoundError` exceptions.
* `task2_write_append.py`: A script that takes user input to write and append data to a text file.
* `sample.txt`: A sample text file used for testing Task 1.
* `output.txt`: The file generated and modified by Task 2.

---

## Task Details

### Task 1: Read a File and Handle Errors
This script attempts to open a file named `sample.txt`. 
* **Functionality**: If the file exists, it prints the content with line numbers.
* **Error Handling**: If the file is missing, it catches the `FileNotFoundError` and displays a user-friendly message instead of crashing.

### Task 2: Write and Append Data to a File
This script demonstrates the difference between "Write" mode and "Append" mode.
* **Step 1**: Takes user input and uses `'w'` mode to create/overwrite `output.txt`.
* **Step 2**: Takes a second input and uses `'a'` mode to add data to the end of the file without deleting the previous content.
* **Step 3**: Reads the entire file to display the final result.

---

## How to Run

1.  **Clone the repository**:
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    ```
2.  **Navigate to the folder**:
    ```bash
    cd your-repo-name
    ```
3.  **Run the scripts**:
    ```bash
    python task1_read_handle.py
    python task2_write_append.py
    ```

## Skills Demonstrated
* Python File I/O (`open()`, `read()`, `write()`, `append`)
* Exception Handling (`try-except` blocks)
* Context Managers (`with` statement)
* User Input Processing
