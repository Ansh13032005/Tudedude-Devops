# Python Assignment

This repository contains solutions for basic Python programming tasks including conditional statements, dictionaries, and file handling operations.

## Assignment Questions

### 1. Grade Checker

#### Problem Statement
Take a score as input and print the grade based on the following criteria:

| Score Range | Grade |
|-------------|-------|
| 90+ | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| Below 60 | F |

#### Python Code
```python
score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

#### Explanation
This program takes marks as input and uses `if-elif-else` statements to determine the grade.

---

### 2. Student Grades Dictionary

#### Problem Statement
Create a dictionary where:
- Key = Student Name
- Value = Grade

Allow the user to:
- Add a student
- Update a student's grade
- Print all student grades

#### Python Code
```python
students = {}

while True:
    print("\n1. Add Student")
    print("2. Update Grade")
    print("3. Display Grades")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade
        print("Student added successfully!")

    elif choice == "2":
        name = input("Enter student name to update: ")

        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print("Grade updated successfully!")
        else:
            print("Student not found!")

    elif choice == "3":
        print("\nStudent Grades:")
        for name, grade in students.items():
            print(name, ":", grade)

    elif choice == "4":
        print("Program exited.")
        break

    else:
        print("Invalid choice!")
```

#### Explanation
This program uses a dictionary to store student names and grades. Users can add, update, and display records.

---

### 3. Write to a File

#### Problem Statement
Create a text file and write content into it.

#### Python Code
```python
file = open("sample.txt", "w")

file.write("Hello, this is a sample file.\n")
file.write("Python file handling example.")

file.close()

print("Content written successfully!")
```

#### Explanation
This program creates a file and writes text using `open()` and `write()`.

---

### 4. Read from a File

#### Problem Statement
Read content from a file and display it.

#### Python Code
```python
file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()
```

#### Explanation
This program opens a file in read mode and displays its contents.

---

## Project Structure

```plaintext
Python-Assignment/
│── screenshots/
│   ├── grade_checker.png
│   ├── student_grades.png
│   ├── write_file.png
│   ├── read_file.png
│
│── grade_checker.py
│── student_grades.py
│── write_file.py
│── read_file.py
│── README.md
│── assignment.docx
```

## Screenshots
Screenshots of code execution and outputs are included in the `screenshots` folder.

## Technologies Used
- Python 3
- VS Code / PyCharm
- Git & GitHub

## Author
**Ansh Parikh**