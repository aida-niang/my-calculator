import math

def perform_operation(a, b, operator):
    """Performs the specified operation between two numbers."""
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b
    else:
        raise ValueError(f"Invalid operator: {operator}")

def scientific_calculator(function, value):
    """Performs scientific calculations on a single value."""
    try:
        if function == 'sin':
            return math.sin(math.radians(value))
        elif function == 'cos':
            return math.cos(math.radians(value))
        elif function == 'tan':
            return math.tan(math.radians(value))
        elif function == 'log':
            if value <= 0:
                raise ValueError("Logarithm undefined for non-positive values.")
            return math.log(value)
        elif function == 'sqrt':
            if value < 0:
                raise ValueError("Square root undefined for negative values.")
            return math.sqrt(value)
        else:
            raise ValueError(f"Invalid scientific function: {function}")
    except ValueError as e:
        raise ValueError(e)

def evaluate_expression(expression):
    """Evaluates a mathematical expression while respecting operator precedence."""
    elements = expression.split()

    # Handle multiplication and division first
    i = 0
    while i < len(elements):
        if elements[i] in ('*', '/'):
            operator = elements[i]
            a = float(elements[i - 1])
            b = float(elements[i + 1])
            result = perform_operation(a, b, operator)
            elements[i - 1:i + 2] = [str(result)]
            i -= 1
        else:
            i += 1

    # Handle addition and subtraction
    i = 0
    while i < len(elements):
        if elements[i] in ('+', '-'):
            operator = elements[i]
            a = float(elements[i - 1])
            b = float(elements[i + 1])
            result = perform_operation(a, b, operator)
            elements[i - 1:i + 2] = [str(result)]
            i -= 1
        else:
            i += 1

    return float(elements[0])

def ask_for_expression():
    """Prompts the user to input a mathematical expression."""
    print("Welcome to the calculator!")
    print("Enter a mathematical expression with spaces between numbers and operators.")
    print("Example: 3 + 5 * 2")

    while True:
        try:
            mode = input("Choose mode: 'basic' for basic operations or 'scientific' for scientific calculations: ").lower()
            if mode == 'basic':
                expression = input("Enter your expression: ")

                if not all(c.isdigit() or c.isspace() or c in '+-*/.' for c in expression):
                    raise ValueError("The expression contains invalid characters.")
                result = evaluate_expression(expression)
                print(f"The result is: {result}")
            elif mode == 'scientific':
                function = input("Enter scientific function (sin, cos, tan, log, sqrt): ").lower()
                value = float(input("Enter the value: "))
                result = scientific_calculator(function, value)
                print(f"The result of {function}({value}) is: {result}")
            else:
                print("Invalid mode selected. Please choose 'basic' or 'scientific'.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        continue_calculation = input("Do you want to perform another calculation? (y/n): ").lower()
        if continue_calculation != 'y':
            print("Thank you for using the calculator. Goodbye!")
            break

# Run the program
ask_for_expression()
