"""unbreakable.py - a small calculator that never crashes on bad input."""


def read_number(prompt):
    """Keep asking until the user types a valid whole number."""
    while True:
        text = input(prompt)
        try:
            return int(text)
        except ValueError:
            print(f"'{text}' is not a number. Please try again.")


def divide(a, b):
    """Return a / b, or a friendly message if b is zero."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


def main():
    print("Unbreakable divider (press Ctrl+C to quit)")
    try:
        while True:
            a = read_number("Enter the first number: ")
            b = read_number("Enter the second number: ")
            print(f"Result: {divide(a, b)}\n")
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")


if __name__ == "__main__":
    main()