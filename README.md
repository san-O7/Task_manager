# Python Task Manager

A simple command-line task management application built with Python. Users can create, view, edit, and delete tasks, assign priority levels, and save their tasks locally using JSON.

This project was developed to practice Python fundamentals, file handling, data structures, input validation, and building functional command-line applications.

## Features

- **View Tasks** — Display all saved tasks with their priority levels.
- **Add Tasks** — Create new tasks with High, Medium, or Low priority.
- **Edit Tasks** — Update the title of an existing task.
- **Delete Tasks** — Remove tasks from the list.
- **Change Priority** — Modify the priority of an existing task.
- **Persistent Storage** — Automatically save changes to a JSON file and load tasks when the application starts.
- **Input Validation** — Handle invalid menu options, task numbers, empty titles, and unsupported priorities.

## Technologies Used

- **Python 3** — Main programming language
- **JSON** — Local data storage
- **Python Standard Library** — No external dependencies required

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/san-O7/python-task-manager.git
```

**2. Navigate to the project directory**

```bash
cd python-task-manager
```

**3. Run the application**

```bash
python main.py
```

On some Windows installations, use `py main.py` instead.

## How to Use

When you run the application, the following menu appears:

```text
1. View tasks
2. Add task
3. Edit task
4. Delete task
5. Change priority
6. Exit
```

Enter the number corresponding to your desired action.

### Example: Adding a Task

```text
Choose an option: 2
Add task: Study Python
Choose priority (High/Medium/Low): High

Task added successfully!
```

### Example: Viewing Tasks

```text
1) [High] Study Python
-----------------------------------------------
2) [Medium] Finish assignment
-----------------------------------------------
3) [Low] Clean room
-----------------------------------------------
```

### Example: Changing Priority

```text
Choose an option: 5
Which task priority to change: 1
Select new priority (High/Medium/Low): Low

Priority changed successfully!
```

## Project Structure

```text
python-task-manager/
├── main.py
├── tasks.json
└── README.md
```

- `main.py` — Contains the application's logic and command-line interface.
- `tasks.json` — Stores saved tasks and is created automatically when tasks are saved.
- `README.md` — Project documentation.

## Data Storage

Tasks are stored in a JSON file in the following format:

```json
[
    {
        "title": "Study Python",
        "priority": "High"
    },
    {
        "title": "Finish assignment",
        "priority": "Medium"
    }
]
```

Changes are saved automatically after successfully adding, editing, or deleting tasks, or changing a priority.

When the application restarts, previously saved tasks are loaded from `tasks.json`.

## What I Learned

Through this project, I practiced:

- Working with Python lists and dictionaries
- Creating reusable functions
- Using loops and conditional statements
- Handling user input and validating data
- Reading and writing JSON files
- Using exception handling to prevent crashes
- Organizing a command-line Python application
- Testing application functionality and edge cases

## Future Improvements

Potential features for future versions include:

- Marking tasks as completed
- Adding due dates
- Sorting and filtering tasks by priority
- Searching for tasks by title
- Adding automated unit tests
- Replacing JSON storage with SQLite
- Creating a graphical interface

## Project Purpose

This project is part of my Python learning journey and serves as a foundation for more advanced software development and AI engineering projects.

It demonstrates fundamental programming concepts and practical problem-solving through a functional application.
