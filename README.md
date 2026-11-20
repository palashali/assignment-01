# Python Practice Assignment

This repository contains solutions to two Python practice problems covering user input, f-strings, arithmetic operations, conditional logic, and input validation.

## Repository Structure

```text
python-practice-assignment/
├── personal_calculator.py
├── grade_calculator.py
└── README.md
```

## Practice Problems

### 1. Personal Information & Simple Calculator (`personal_calculator.py`)
- Prompts the user for their name, age, and two numbers.
- Calculates and displays addition, subtraction, multiplication, and division using f-strings.
- Handles division by zero safely.

**Run:**
```bash
python3 personal_calculator.py
```

**Example Output:**
```text
Enter your name: Rahim
Enter your age: 22
Enter first number: 20
Enter second number: 10
Hello, Rahim!
Your age is 22.
Addition: 30
Subtraction: 10
Multiplication: 200
Division: 2.0
```

### 2. Student Grade Calculator (`grade_calculator.py`)
- Prompts for a student's name and marks for Math, English, and Python.
- Validates that all marks are between `0` and `100`.
- Calculates the average marks (to 2 decimal places) and assigns a final grade:
  - `80–100`: `A+`
  - `70–79`: `A`
  - `60–69`: `A-`
  - `50–59`: `B`
  - `40–49`: `C`
  - `Below 40`: `F`

**Run:**
```bash
python3 grade_calculator.py
```

**Example Output:**
```text
Enter student name: Rahim
Enter Math marks: 85
Enter English marks: 75
Enter Python marks: 90
Student Name: Rahim
Average Marks: 83.33
Final Grade: A+
```
