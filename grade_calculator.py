def calculate_grade(average: float) -> str:
    """Return the letter grade based on average marks."""
    if average >= 80:
        return "A+"
    elif average >= 70:
        return "A"
    elif average >= 60:
        return "A-"
    elif average >= 50:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "F"


def main():
    name = input("Enter student name: ").strip()
    math_marks = float(input("Enter Math marks: "))
    english_marks = float(input("Enter English marks: "))
    python_marks = float(input("Enter Python marks: "))

    marks = [math_marks, english_marks, python_marks]
    if any(mark < 0 or mark > 100 for mark in marks):
        print("Invalid marks! Marks for each subject must be between 0 and 100.")
        return

    average = sum(marks) / len(marks)
    grade = calculate_grade(average)

    print(f"Student Name: {name}")
    print(f"Average Marks: {average:.2f}")
    print(f"Final Grade: {grade}")


if __name__ == "__main__":
    main()
