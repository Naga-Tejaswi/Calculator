"""
Calculator CLI App
Author: Elevate Labs
Description: A professional command-line calculator supporting basic operations.
"""

def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract two numbers."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide two numbers. Raises ValueError on division by zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def get_number(prompt):
    """Prompt the user for a number and validate input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    operations = {
        '1': (add, 'Addition'),
        '2': (subtract, 'Subtraction'),
        '3': (multiply, 'Multiplication'),
        '4': (divide, 'Division')
    }

    while True:
        print("\nCalculator Menu:")
        for key, (_, name) in operations.items():
            print(f"{key}. {name}")
        print("5. Exit")

        choice = input("Select an operation (1-5): ").strip()

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break
        elif choice in operations:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            func, name = operations[choice]
            try:
                result = func(num1, num2)
                print(f"Result of {name}: {result}")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
