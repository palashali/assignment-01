def parse_number(value: str):
    """Convert numeric input to int if it is a whole number, otherwise float."""
    num = float(value)
    return int(num) if num.is_integer() else num


def main():
    name = input("Enter your name: ").strip()
    age = int(input("Enter your age: "))
    num1 = parse_number(input("Enter first number: "))
    num2 = parse_number(input("Enter second number: "))

    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2

    print(f"Hello, {name}!")
    print(f"Your age is {age}.")
    print(f"Addition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")

    if num2 != 0:
        division = num1 / num2
        print(f"Division: {division}")
    else:
        print("Division: Cannot divide by zero")


if __name__ == "__main__":
    main()
