# Codveda Python Development Internship – Level 2

## Overview

This repository contains the projects completed as part of the
Level 2 (Intermediate) tasks for the Python Development Internship
at Codveda Technology.

The projects focus on applying Python programming concepts to
develop practical command-line applications. The tasks demonstrate
working with file storage, JSON data, external APIs, HTTP requests,
error handling, and user interaction.

Two projects have been completed for this level:

1. To-Do List Application
2. Weather Information Application using API Integration

---

# Task 1: To-Do List Application

## Description

The To-Do List Application is a command-line application developed
in Python that allows users to manage their daily tasks.

The application provides options to add new tasks, view existing
tasks, mark tasks as completed, and delete tasks.

The tasks are stored in a JSON file so that the task information
can be saved and accessed even after the application is closed.

## Objectives

The main objectives of this task are:

- To implement the ability to add tasks.
- To display the existing tasks.
- To mark tasks as completed.
- To delete tasks.
- To store task information in a JSON file.
- To implement basic error handling.
- To create an interactive command-line application.

## Features

The application provides the following features:

### 1. Add Task

Users can enter a task description and add it to the task list.

### 2. View Tasks

Users can view all stored tasks along with their current status.

Tasks can have either of the following statuses:

- Pending
- Done

### 3. Mark Task as Completed

Users can select a task using its task number and mark it as
completed.

### 4. Delete Task

Users can select a task number and permanently remove the task
from the list.

### 5. Data Persistence

Tasks are stored in a JSON file named `tasks.json`.

This allows task information to remain available when the program
is restarted.

### 6. Error Handling

The application handles invalid task numbers, empty task names,
and invalid numerical input.

## Technologies Used

- Python 3
- JSON
- `json` module
- `os` module
- Command Line Interface (CLI)

## Python Concepts Used

- Functions
- Lists
- Dictionaries
- Loops
- Conditional statements
- File handling
- JSON data storage
- Exception handling
- User input

## How the Program Works

1. The program starts and loads previously saved tasks from the
   `tasks.json` file.
2. A menu containing different task-management options is displayed.
3. The user selects an option.
4. Depending on the selected option, the user can add, view,
   complete, or delete tasks.
5. Any changes made to the task list are saved to the JSON file.
6. The program continues running until the user chooses the
   Exit option.

## Example

```text
===== TO-DO LIST APPLICATION =====

1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Delete Task
5. Exit

Enter your choice (1-5): 1

Enter the task: Complete Python internship
Task added successfully!