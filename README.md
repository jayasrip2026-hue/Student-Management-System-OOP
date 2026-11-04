# Student Management System — Python OOP Project

A beginner-friendly, menu-driven Student Management System built using Python.
It demonstrates object-oriented programming concepts and saves student records
locally in a JSON file.

## Features
- Add regular or graduate student records
- Display all students and grades
- Search by roll number
- Update marks
- Delete student records
- Persistent JSON file storage
- Input validation

## OOP Concepts
- **Classes and objects:** `Student`, `GraduateStudent`, `StudentManager`
- **Encapsulation:** private-style attributes (`_roll_no`, `_name`, `_marks`) and properties
- **Inheritance:** `GraduateStudent` inherits from `Student`
- **Polymorphism:** `GraduateStudent` overrides `calculate_grade()` and `student_type()`
- **Constructor:** `__init__()`

## Requirements
Python 3.8 or later. No external packages are required.

## How to Run
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python main.py
   ```

   On some systems, use `python3 main.py`.

4. Follow the menu displayed in the terminal.

Student records are stored in `students.json` in the same folder.

## Project Structure
```text
Student_Management_System/
├── main.py
├── students.json
└── README.md
```

## Author
Student project submitted for Python OOP Assessment.
