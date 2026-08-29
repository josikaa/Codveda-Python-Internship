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