# Codveda Python Development Internship – Level 3

## Overview

This repository contains the projects completed as part of the
Level 3 (Advanced) tasks for the Python Development Internship
at Codveda Technology.

The projects focus on applying Python programming concepts to
more advanced problem-solving and security-related applications.

Two projects have been completed for this level:

1. File Encryption and Decryption
2. N-Queens Problem

---

# Task 2: File Encryption and Decryption

## Description

The File Encryption and Decryption application is a Python
command-line program that allows users to securely encrypt and
decrypt text files.

The project uses the Fernet encryption method provided by the
Python `cryptography` library. An encryption key is generated
and stored locally, and the same key is required to decrypt the
encrypted file.

The application allows users to:

- Generate an encryption key
- Encrypt a file
- Decrypt an encrypted file
- Handle missing files
- Handle decryption errors

## Objectives

The main objectives of this task are:

- To allow users to select a file for encryption.
- To encrypt file contents securely.
- To save the encrypted content as a new file.
- To decrypt encrypted files.
- To restore the original file content.
- To implement basic error handling.

## Technologies Used

- Python 3
- `cryptography` library
- Fernet encryption
- File handling
- Command Line Interface (CLI)

## Python Concepts Used

- Functions
- File handling
- Binary file operations
- Conditional statements
- Exception handling
- Modules
- User input

## How the Program Works

1. The user starts the application.
2. An encryption key can be generated.
3. The user selects the encryption option.
4. The program reads the selected file.
5. The file contents are encrypted using Fernet.
6. The encrypted contents are saved with the `.encrypted`
   extension.
7. The user can later select the encrypted file for decryption.
8. The program uses the stored key to decrypt the file.
9. The original content is restored.

## Example

```text
===== File Encryption and Decryption =====

1. Generate Encryption Key
2. Encrypt File
3. Decrypt File
4. Exit

Enter your choice (1-4): 1

Encryption key generated successfully.
Encryption:

Enter your choice (1-4): 2
Enter the file name to encrypt: sample.txt

File encrypted successfully: sample.txt.encrypted

Decryption:

Enter your choice (1-4): 3
Enter the encrypted file name: sample.txt.encrypted

File decrypted successfully: sample.txt
Security Note

The encryption key is required to decrypt the encrypted file.
The secret.key file should be kept private and is excluded
from the GitHub repository using .gitignore.
```
# Task 3: N-Queens Problem
## Description

The N-Queens Problem is a classic algorithmic problem in which
N queens must be placed on an N × N chessboard so that no two
queens can attack each other.

The program uses a backtracking algorithm to find a valid
arrangement of queens.

A valid solution ensures that no two queens share:

The same row
The same column
The same diagonal
## Objectives

The main objectives of this task are:

To represent the chessboard using a two-dimensional array.
To place queens one row at a time.
To check whether a position is safe.
To use backtracking to find a valid solution.
To ensure that no queens attack each other.
To handle invalid user input.
## Technologies Used
Python 3
Two-dimensional lists
Backtracking algorithm
Command Line Interface (CLI)
## Python Concepts Used
Functions
Lists
Nested loops
Conditional statements
Recursion
Backtracking
User input
Exception handling
## How the Algorithm Works
An empty N × N chessboard is created.
The program starts placing queens from the first row.
Before placing a queen, the program checks whether the
position is safe.
If the position is safe, a queen is placed.
The program moves to the next row.
If no safe position is available, the program backtracks
to the previous row.
The previous queen is removed and another position is tried.
The process continues until all queens are placed.
```text
Example

For 4 queens, one possible solution is:

. Q . .
. . . Q
Q . . .
. . Q .

Where:

Q = Queen
. = Empty position

No two queens share the same row, column, or diagonal.
```
# Testing
## File Encryption and Decryption Testing

The encryption project was tested by:

Generating an encryption key.
Encrypting a sample text file.
Confirming that an encrypted file was created.
Decrypting the encrypted file.
Confirming that the original content was restored.
Testing file-not-found handling.
## N-Queens Testing

The N-Queens project was tested using:

N = 4
Invalid numerical input
Positive integer input
Verification of queen positions
# Learning Outcomes

Through the Level 3 projects, the following skills were developed:

Understanding file encryption and decryption.
Working with external Python libraries.
Handling files in binary mode.
Implementing exception handling.
Understanding recursive algorithms.
Applying the backtracking technique.
Solving constraint-based problems.
Developing command-line applications.
Testing programs with different inputs.
# Conclusion

The Level 3 projects provided practical experience with advanced
Python programming concepts.

The File Encryption and Decryption project introduced secure file
processing using Fernet encryption, while the N-Queens project
demonstrated recursive problem solving and backtracking.

Together, these projects strengthened programming, algorithmic
thinking, file handling, security, and problem-solving skills.

# Internship Information

Organization: Codveda Technology
Internship Domain: Python Development
Level: Level 3 – Advanced

# Projects Completed:

File Encryption and Decryption
N-Queens Problem

